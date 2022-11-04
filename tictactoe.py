"""
M. Scott Reynolds
3 November 2022
Tic-Tac-Toe

Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.

Rules
Tic-Tac-Toe is played according to the following rules.

1. The game is played on a grid that is three squares by three squares.
2. Player one uses x's. Player two uses o's.
3. Players take turns putting their marks in empty squares.
4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
5. If all nine squares are full and neither player has three in a row, the game ends in a draw.

Grid

0|1|2
-+-+-
3|4|5
-+-+-
6|7|8

"""

# Define table of winning rows that need to be checked for each squre.
winning_positions = [
    [[1, 2], [3, 6], [4, 8]],           # 0
    [[0, 2], [4, 7]],                   # 1
    [[0, 1], [4, 6], [5, 8]],           # 2
    [[0, 6], [4, 5]],                   # 3
    [[0, 8], [1, 7], [2, 6], [3, 5]],   # 4
    [[2, 8], [3, 4]],                   # 5
    [[0, 3], [2, 4], [7, 8]],           # 6
    [[1, 4], [6, 8]],                   # 7
    [[0, 4], [2, 5], [6, 7]]            # 8
   ]

player_x = "x"
player_o = "o"

def main():
    # Initialize positions.
    positions = \
        ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

    available_positions = count_available_positions(positions)
    a_winner = None
    current_player = player_x
    print("Let's play a game of of tic-tac-toe.")
    print()
    display_positions(positions)
    while available_positions > 0:
        # Loop until no more avaiable positions
        # or a player has won.

        # go for current_player
        choice = get_choice(current_player, positions)
        display_positions(positions)

        a_winner = check_for_win(choice, positions)
        if a_winner:
            print(f"Congratulations, {a_winner} won the game.") 
            break

        # Change current player
        if current_player == player_x:
            current_player = player_o
        else:
            current_player = player_x

        # Now count available positions left.
        available_positions = count_available_positions(positions)

    if not a_winner:
        print("Tie game.")


def count_available_positions(positions):
    # return the number of available positions,
    # not already taken by a player.
    available = 0
    for i in range(9):
        if positions[i] != player_x and positions[i] != player_o:
            available += 1
    return available


def check_for_win(choice, positions):
    # check for a winner at choice.
    # Return the winner if it is a winning position. None otherwise.

    square = choice-1
    a_winner = None
    player = positions[square]

    winning_rows = winning_positions[square]
    for row in winning_rows:
        if positions[row[0]] == player and positions[row[1]] == player:
            a_winner = player
            break
    return a_winner


def get_choice(player, positions):
    # Get a valid choice for the player
    # and return the choice. Note that choice
    # is based on 1 - 9.
    valid_choice = False
    while not valid_choice:
        choice = int(input(f"{player}'s turn to choose a square (1-9): "))
        if choice >= 1 and choice <= 9:
            square = choice-1
            if positions[square] != player_x and positions[square] != player_o:
                positions[square] = player
                valid_choice = True
            else:
                print("Square is already taken. Please try again.")
        else:
            print(f"Invalid choice {choice}. Please try again.")
    print()
    return choice


# Display the positions
def display_positions(positions):
    print(f"{positions[0]}|{positions[1]}|{positions[2]}")
    print("-+-+-")
    print(f"{positions[3]}|{positions[4]}|{positions[5]}")
    print("-+-+-")
    print(f"{positions[6]}|{positions[7]}|{positions[8]}")
    print()


# Call main to start this program.
if __name__ == "__main__":
    main()
