# ISSUE 31
#
# Problem:
# Write a program that accepts player names and their scores from multiple matches and calculates each player's total score and ranking.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def player_rankings(players):
    rows = []
    for player in players:
        # TODO: Check that every match score contributes to the total.
        total = sum(player["scores"][1:])
        rows.append({"name": player["name"], "total": total})
    # TODO: Check whether highest totals come first.
    rows.sort(key=lambda row: row["total"])
    for place, row in enumerate(rows, 1):
        # TODO: Check which ranking value is stored for each player.
        # TODO: Check how the place number maps to the player's rank.
        row["rank"] = place + 1
    # TODO: Check that tied scores are handled consistently.
    return rows

def check_solution():
    players = [{"name":"Ari","scores":[5,10,15]},{"name":"Bo","scores":[20,10]}]
    result = player_rankings(players)
    assert result == [{"name":"Ari","total":30,"rank":1},{"name":"Bo","total":30,"rank":2}]
    assert player_rankings([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
