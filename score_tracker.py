#Name of the game
game=input("Please enter the name of the game we are playing!  ").title()
winning_rule=input("Who wins this game: highest points or lowest points?\nPlease enter either 'highest' or lowest' ")

#Number of rounds
rounds_quantity=int(input(f"How many rounds does {game} have? "))

#number of players
players_quantity=int(input("Please enter the number of players: "))

#Players names
players=[input(f"Please enter player {i + 1}'s name: ").capitalize() for i in range(players_quantity)]

#Game reset
player_cumulative = {player: 0 for player in players}

#starting the game
for round_number in range(1, rounds_quantity + 1):
    print(f"\n\nRound {round_number}")
    print("\n Scores this round:")
    
    #player scores
    # Input scores for each player and update cumulative scores
    for player in players:
        score = int(input(f"{player}, what was your score: "))
        player_cumulative[player] += score

    print("\nCumulative Scores:")
    for player in players:
        print(f"{player}: {player_cumulative[player]} points.")

#declaring a winner
if winning_rule == 'highest':
    winner = max(player_cumulative, key=player_cumulative.get)
    print(f"\nThe winner is {winner} with {player_cumulative[winner]} points!")

elif winning_rule == 'lowest':
    winner = min(player_cumulative, key=player_cumulative.get)
    print(f"\nThe winner is {winner} with {player_cumulative[winner]} points!")

else:
    print("Invalid winning rule, figure it out.")

