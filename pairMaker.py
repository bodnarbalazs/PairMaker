from __future__ import annotations

from ortools.sat.python import cp_model
from typing import List, Tuple

from player import Player

def _norm(val: int) -> float:
    """Normalize a 1-3 scale value → 0-1 scale (inclusive)."""
    return val / 3.0


def pair_breakdown(p1: Player, p2: Player):
    """Return detailed strength breakdown for a (p1, p2) pair as a dict."""
    n_p1_serve = _norm(p1.serve)
    n_p1_base = _norm(p1.base_swing)
    n_p1_net = _norm(p1.net_work)
    n_p2_serve = _norm(p2.serve)
    n_p2_base = _norm(p2.base_swing)
    n_p2_net = _norm(p2.net_work)

    # Components
    comp_p1_serves = (n_p1_serve + n_p1_base + 0.5) * (n_p2_net + 1)
    comp_p2_serves = (n_p2_serve + n_p2_base + 0.5) * (n_p1_net + 1)
    comp_opponent_serves = (n_p1_base + 1) * (n_p2_net + 1) + (n_p2_base + 1) * (n_p1_net + 1)

    bonus = (
        p1.is_fast + p2.is_fast + p1.is_balanced + p2.is_balanced + p1.is_cunning + p2.is_cunning
    )

    penalties = 0
    if p1.is_fast == 0 and p2.is_fast == 0:
        penalties += 1
    if p1.is_balanced == 0 and p2.is_balanced == 0:
        penalties += 1

    total = comp_p1_serves + comp_p2_serves + comp_opponent_serves + bonus - penalties

    return {
        "p1_serves": comp_p1_serves,
        "p2_serves": comp_p2_serves,
        "opponent_serves": comp_opponent_serves,
        "bonus": bonus,
        "penalties": penalties,
        "total": total,
    }


def _pair_strength(p1: Player, p2: Player) -> int:
    """Wrapper around ``pair_breakdown`` returning an int ×100 for CP-SAT."""
    total = pair_breakdown(p1, p2)["total"]
    return int(round(total * 100))


def optimal_team_assignment(players: List[Player], group_count: int = 1, top_k: int = 1):
    """Find an assignment of players into *group_count* groups of pairs.

    Each player appears in exactly one pair.  Groups can have different sizes.
    The objective is to minimise the *sum* over groups of (max_strength - min_strength).
    A player's ``group`` attribute can fix them to a specific group (≥0) or -1 for free.
    """
    assert len(players) % 2 == 0, "Must be even number of players"
    n = len(players)
    num_teams = n // 2

    model = cp_model.CpModel()
    x = {}  # x[i][j] = 1 if players i and j are in a team

    # Pre-compute pair strengths and decision vars
    pair_strength_value = {}
    for i in range(n):
        for j in range(i + 1, n):
            x[(i, j)] = model.NewBoolVar(f"x_{i}_{j}")
            pair_strength_value[(i, j)] = _pair_strength(players[i], players[j])
            # Enforce dislike constraints
            if players[i].dislikes_player(players[j]) or players[j].dislikes_player(players[i]):
                model.Add(x[(i, j)] == 0)

    # Player-to-group assignment variables (one-hot)
    g = {}
    for i in range(n):
        for k in range(group_count):
            g[(i, k)] = model.NewBoolVar(f"g_{i}_{k}")
        model.Add(sum(g[(i, k)] for k in range(group_count)) == 1)  # one group per player
        if players[i].group >= 0:
            # fixed group
            for k in range(group_count):
                if k == players[i].group:
                    model.Add(g[(i, k)] == 1)
                else:
                    model.Add(g[(i, k)] == 0)

    # Link pair selection to common group via auxiliary y[i,j,k]
    y = {}
    for (i, j), pair_var in x.items():
        for k in range(group_count):
            y[(i, j, k)] = model.NewBoolVar(f"y_{i}_{j}_{k}")
            # y implies pair chosen and both players in group k
            model.Add(y[(i, j, k)] <= pair_var)
            model.Add(y[(i, j, k)] <= g[(i, k)])
            model.Add(y[(i, j, k)] <= g[(j, k)])
            # If pair chosen and both players in group, y can be 1: ensure consistency
            model.Add(pair_var + g[(i, k)] + g[(j, k)] - 2 <= y[(i, j, k)])
        # Ensure pair is assigned to exactly one group when chosen
        model.Add(sum(y[(i, j, k)] for k in range(group_count)) == pair_var)


    # Each player appears in exactly one pair (across all groups)
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

    # Group-specific max / min
    max_strength_g = {}
    min_strength_g = {}
    for k in range(group_count):
        max_strength_g[k] = model.NewIntVar(0, total_strength_cap, f"max_strength_{k}")
        min_strength_g[k] = model.NewIntVar(0, total_strength_cap, f"min_strength_{k}")
        model.Add(min_strength_g[k] <= max_strength_g[k])

    # Strength variables per pair per group with conditional bounds
    for (i, j), base_ts_var in team_strengths.items():
        for k in range(group_count):
            indicator = y[(i, j, k)]
            # pair strength variable equals base only if indicator true, else 0
            ts_g = model.NewIntVar(0, total_strength_cap, f"ts_{i}_{j}_{k}")
            model.Add(ts_g == base_ts_var).OnlyEnforceIf(indicator)
            model.Add(ts_g == 0).OnlyEnforceIf(indicator.Not())
            # bind to group max/min
            model.Add(ts_g <= max_strength_g[k]).OnlyEnforceIf(indicator)
            model.Add(ts_g >= min_strength_g[k]).OnlyEnforceIf(indicator)

    # Objective: minimise sum over groups of spreads
    model.Minimize(sum(max_strength_g[k] - min_strength_g[k] for k in range(group_count)))

    # Collect up to top_k solutions by iterative blocking.
    solutions = []
    iteration = 0
    while iteration < top_k:
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = 10.0
        status = solver.Solve(model)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            break  # no more solutions

        # --- extract solution ---
        teams_by_group = {k: [] for k in range(group_count)}
        chosen_pairs = []
        for (i, j), var in x.items():
            if solver.Value(var):
                chosen_pairs.append((i, j))
                for k in range(group_count):
                    if solver.Value(y[(i, j, k)]):
                        teams_by_group[k].append((players[i], players[j]))
                        break
        solutions.append(
            {
                "groups": teams_by_group,
                "spread_per_group": {
                    k: (solver.Value(max_strength_g[k]) - solver.Value(min_strength_g[k])) / 100.0
                    for k in range(group_count)
                },
                "objective": solver.ObjectiveValue() / 100.0,
            }
        )

        # --- add blocking constraint to forbid this exact assignment ---
        model.Add(sum(x[pair] for pair in chosen_pairs) <= len(chosen_pairs) - 1)
        iteration += 1

    return solutions if solutions else None
