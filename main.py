from player import Player
from pairMaker import optimal_team_assignment, pair_breakdown

players = Player.load_csv("sample_players.csv")
result = optimal_team_assignment(players)

if result:
    print("Team assignments (index, Player):")
    for team in result["teams"]:
        (_, p1), (_, p2) = team
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
    print(f"Max team strength: {result['max_strength']:.2f}")
    print(f"Min team strength: {result['min_strength']:.2f}")
    print(f"Difference: {result['diff']:.2f}")
else:
    print("No solution found")
