#Tic Tac Toe Game in Python

def main():
    markers = pickMarker()

    # Ask players if they are ready to play
    ready = ""
    while ready not in ['YES', 'NO']:
        ready = input("Are you ready to play? Enter Yes or No: ").upper()
    
    # If not ready, close the program
    if ready == 'NO':
        print("Goodbye.")
        return 0
    # Players are ready to play
    else:
        playGame(markers)
        
def pickMarker():
    """
    Function returns marker choices for Player 1 and Player 2 as a dictionary
    """
    markers = {1: "", 2: ""}

    # Get input from Player 1
    while markers[1] not in ['X', 'O']:
        markers[1] = input("Player 1: Do you want to be X or O?: ").upper()
    
    print(f"Player 1 ('{markers[1]}') will go first")

    # Assign marker to Player 2
    markers[2] = 'O' if markers[1] == 'X' else 'X'

    return markers

def playGame(markers):
    """
    Summary- Function goes through the gameflow of the tic tac toe game
    
    Arguments:
        markers- A dictionary of Player 1 and 2 markers ('X' and 'O')
    """
    # Mark the grid with values from 1-9 (exclude 0)
    # 0 will not be used- it is included so that indices and grid numbers are equal ie index 1 = grid value 1
    playerInput = [i for i in range(10)]

    displayGrid(playerInput)
    
    turn = 1 # Tracks which player's move it is currently
    loc = 0 # Accepts player input regarding where to make their move
    filled = [] # Keeps track of tic tac toe grid locations that have already been played

    while True:
        # Accept player input regarding where to make their move
        loc = int(input(f"\n\nPlayer {turn}, your move: "))

        # Check if move is invalid
        if loc < 1 or loc > 9 or loc in filled:
            print("Invalid Move.")
        
        # If move is valid...
        else:
            filled.append(loc) # Add move to list of filled locations
            playerInput[loc] = markers[turn] # Update player input grid index with player marker
            displayGrid(playerInput)

            gameStatus(playerInput, turn, filled) # Determine if game is won or drawn yet

            # Switch turns from player 1 to 2 or vice versa
            turn = 2 if turn == 1 else 1


def displayGrid(playerInput):
    """
    Summary- Function takes in a list of playerInputs and displays them into a tic tac toe grid
    
    Arguments:
        playerInput: A list of player input values. Numbered 1-9 by default (0 is unused)
                    Contains 'X' or '0' in indices that have been played by the players
    """
    print('\n')
    print(f' {playerInput[7]} | {playerInput[8]} | {playerInput[9]}')
    print('---|---|---')
    print(f' {playerInput[4]} | {playerInput[5]} | {playerInput[6]}')
    print('---|---|---')
    print(f' {playerInput[1]} | {playerInput[2]} | {playerInput[3]}')

def gameStatus(playerInput, turn, filled):
    """
    Summary- Function determines if a game has been won or drawn and restarts the game if so.
    
    Arguments:
        playerInput: A list of player input values.
        turn: Determine which players move it is by using the %2 operator along with it
        filled- a list of tic tac toe locations that have already been used (Cannot be overridden)
    """
    # Check if any player has occupied 3 consecutive blocks
    if playerInput[1] == playerInput[5] == playerInput[9] or \
    playerInput[3] == playerInput[5] == playerInput[7] or \
    playerInput[1] == playerInput[2] == playerInput[3] or \
    playerInput[4] == playerInput[5] == playerInput[6] or \
    playerInput[7] == playerInput[8] == playerInput[9] or \
    playerInput[1] == playerInput[4] == playerInput[7] or \
    playerInput[2] == playerInput[5] == playerInput[8] or \
    playerInput[3] == playerInput[6] == playerInput[9]:
        # If yes, they win
        print(f"\nCongratulations, Player {turn} wins!\n\n")
        main() # Restart game
    
    # If neither player has won, but all squares have been filled up, then it's a draw
    if len(filled) == 9:
        print("\nIt's a draw!\n\n")
        main()

main()