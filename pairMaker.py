from __future__ import annotations

from ortools.sat.python import cp_model
from typing import List, Tuple

from player import Player

def _norm(val: int) -> float:
    """Normalize a 1-3 scale value → 0-1 scale (inclusive)."""
    return val / 3.0


def _pair_strength(p1: Player, p2: Player) -> int:
    """Compute pair strength using the new model; returns an *integer* score.

    The formula contains fractional terms; multiply final value by 100 and
    round so we can work with an integer CP-SAT model.
    """
    # Normalize 1-3 attributes
    norm_p1_serve = _norm(p1.serve)
    norm_p1_base = _norm(p1.base_swing)
    norm_p1_net = _norm(p1.net_work)

    norm_p2_serve = _norm(p2.serve)
    norm_p2_base = _norm(p2.base_swing)
    norm_p2_net = _norm(p2.net_work)

    score = (
        (norm_p1_serve + norm_p1_base + 0.5) * (norm_p2_net + 1)
        + (norm_p1_base + 1) * (norm_p2_net + 1)
        + (norm_p2_base + 1) * (norm_p1_net + 1)
        + (norm_p2_serve + norm_p2_base + 0.5) * (norm_p1_net + 1)
        + p1.is_fast + p2.is_fast
        + p1.is_balanced + p2.is_balanced
        + p1.is_cunning + p2.is_cunning
    )

    # Penalties
    if p1.is_fast == 0 and p2.is_fast == 0:
        score -= 1
    if p1.is_balanced == 0 and p2.is_balanced == 0:
        score -= 1

    # Scale to int (×100) for CP-SAT integer vars
    return int(round(score * 100))


def optimal_team_assignment(players: List[Player]):
    """Find an assignment of players into pairs minimizing strength difference.

    Parameters
    ----------
    players : List[Player]
        Even-sized list of Player objects.
    """
    assert len(players) % 2 == 0, "Must be even number of players"
    n = len(players)
    num_teams = n // 2

    model = cp_model.CpModel()
    x = {}  # x[i][j] = 1 if players i and j are in a team

    # Pre-compute pair strengths and create decision variables for each pair
    pair_strength_value = {}
    for i in range(n):
        for j in range(i + 1, n):
            x[(i, j)] = model.NewBoolVar(f"x_{i}_{j}")
            pair_strength_value[(i, j)] = _pair_strength(players[i], players[j])
            # Enforce dislike constraints: if either player refuses the other, forbid the pair
            if players[i].dislikes_player(players[j]) or players[j].dislikes_player(players[i]):
                model.Add(x[(i, j)] == 0)

    # Each player appears in exactly one pair
    for i in range(n):
        model.Add(sum(x[min(i, j), max(i, j)] for j in range(n) if i != j) == 1)

    # Create team strength variables keyed by pair
    team_strengths = {}
    total_strength_cap = max(pair_strength_value.values()) * num_teams
    for (i, j), var in x.items():
        pair_strength = pair_strength_value[(i, j)]
        ts = model.NewIntVar(0, total_strength_cap, f"team_strength_{i}_{j}")
        # If the pair is chosen (var == 1) then ts equals the pair strength,
        # otherwise ts is forced to 0 so that it does not influence min/max.
        model.Add(ts == pair_strength).OnlyEnforceIf(var)
        model.Add(ts == 0).OnlyEnforceIf(var.Not())
        team_strengths[(i, j)] = ts

    # Define max and min team strength over CHOSEN teams only
    max_strength = model.NewIntVar(0, total_strength_cap, "max_strength")
    min_strength = model.NewIntVar(0, total_strength_cap, "min_strength")

    # Link min/max strength only to selected pairs by using conditional constraints
    for (i, j), var in x.items():
        ts = team_strengths[(i, j)]
        # If the pair is selected, it must respect the current max/min bounds
        model.Add(ts <= max_strength).OnlyEnforceIf(var)
        model.Add(ts >= min_strength).OnlyEnforceIf(var)

    # Ensure min_strength is never greater than max_strength (optional safety)
    model.Add(min_strength <= max_strength)

    # Objective: minimize difference
    model.Minimize(max_strength - min_strength)

    # Solve
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10.0
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        teams = []
        for (i, j), var in x.items():
            if solver.Value(var):
                teams.append(((i, players[i]), (j, players[j])))
        return {
            "teams": teams,
            "max_strength": solver.Value(max_strength) / 100.0,
            "min_strength": solver.Value(min_strength) / 100.0,
            "diff": solver.Value(max_strength - min_strength) / 100.0
        }
    else:
        return None
