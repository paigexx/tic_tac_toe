# ----- global variables

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

position_board = ["1","2","3",
                  "4","5","6",
                  "7","8","9",]

game_still_going = True

winner = None

current_player = "X"

# ---- functions

#show an example of the board with the user choice position
def display_position_board():
        print(position_board[0] + " | " + position_board[1] + " | " + position_board[2])
        print(position_board[3] + " | " + position_board[4] + " | " + position_board[5])
        print(position_board[6] + " | " + position_board[7] + " | " + position_board[8])

#the game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Main function and sequence for the gam
#*****
def play_game():
# Introduction to the game and instructions.
    print("Instructions:")
    print("Use this board as a position reference. You will choose a position 1-9.")
    display_position_board()
    print(" ")
    input("Press enter to continue...")


    #Display the initial board
    print(" ")

    display_board()

    while game_still_going:

        handle_turn()

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

#********






# Handle turn
#___________________________
def handle_turn():
    global current_player
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")

# Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:
# Make sure the input is valid
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
# Get correct index in our board list
        position = int(position) - 1

# Then also make sure the spot is available on the board
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
# Put the game piece on the board
        board[position] = current_player
# Show the game board
        display_board()


#___________________________

# Check who is the winner by checking column, rows and diagonals.

def check_if_game_over():
    check_winner()
    check_tie()

def check_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_tie():
# Set global variables
    global game_still_going
# If board is full
    if "-" not in board:
        game_still_going = False
        return True
# Else there is no tie
    else:
        return False

#Check if game is still active by finding a winner
def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    else:
        return None

def check_tie():
# Set global variables
    global game_still_going
# If board is full
    if "-" not in board:
        game_still_going = False
        return True
# Else there is no tie
    else:
        return False

def check_column():
    global game_still_going

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
        # Or return None if there was no winner
    else:
        return None

def check_diagonals():
    global game_still_going

    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"


    if dia_1 or dia_2:
        game_still_going = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]
        # Or return None if there was no winner
    else:
        return None

def flip_player():

    global current_player

    if current_player == ("X"):
        current_player = ("O")

    elif current_player == ("O"):
        current_player = ("X")






#board (c)
#display board fun (c)
# play game fun
# handle turn
# check win
    #check row
    #check columns
    #check diagonals
# check tie
# flip player

play_game()