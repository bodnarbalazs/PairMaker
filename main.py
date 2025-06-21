from player import Player
from pairMaker import optimal_team_assignment, pair_breakdown

players = Player.load_csv("players.csv")
try:
    group_count = int(input("Enter number of groups (default 1): ") or 1)
except (ValueError, EOFError):
    group_count = 1
try:
    top_k = int(input("How many top solutions? (default 1): ") or 1)
except (ValueError, EOFError):
    top_k = 1

results = optimal_team_assignment(players, group_count, top_k)

if results:
    for idx, result in enumerate(results, 1):
        print(f"\n===== Solution #{idx} | Objective: {result['objective']:.2f} =====")
        for k, pairs in result["groups"].items():
            print(f"\nGroup {k} (pairs {len(pairs)}, spread {result['spread_per_group'][k]:.2f})")
            for p1, p2 in pairs:
                bd = pair_breakdown(p1, p2)
                # Header
                print(f"\n{p1.name}  ↔  {p2.name}")
                print("-" * 50)
                # Points table
                rows = [
                    ("p1 serves", bd["p1_serves"]),
                    ("p2 serves", bd["p2_serves"]),
                    ("opponent serves", bd["opponent_serves"]),
                    ("bonus", bd["bonus"]),
                    ("penalties", -bd["penalties"]),
                    ("TOTAL", bd["total"]),
                ]
                col_width = max(len(r[0]) for r in rows) + 2
                for label, val in rows:
                    print(f"{label.ljust(col_width)} {val:6.2f}")
else:
    print("No solution found")
