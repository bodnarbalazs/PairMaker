from player import Player
from pairMaker import optimal_team_assignment

players = Player.load_csv("sample_players.csv")
result = optimal_team_assignment(players)

if result:
    print("Team assignments (index, Player):")
    for team in result["teams"]:
        (i, p1), (j, p2) = team
        print(f"({i}) {p1.name}  ↔  ({j}) {p2.name}")
    print(f"Max team strength: {result['max_strength']:.2f}")
    print(f"Min team strength: {result['min_strength']:.2f}")
    print(f"Difference: {result['diff']:.2f}")
else:
    print("No solution found")
