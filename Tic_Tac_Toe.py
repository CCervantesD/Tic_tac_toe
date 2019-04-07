#-----Global Variables------

#display game board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]


#game still going
game_still_going = True

#who won or tie
winner = None

#who's turn is it
current_player = "X"


#----non global variables----

def play_game():

  # Show the initial game board
  display_board()

  # Loop until the game stops (winner or tie)
  while game_still_going:

    # Handle a turn
    handle_turn(current_player)

    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()

  if winner == "X" or winner == "O":
      print(winner + " won.")
  elif winner == None:
      print("Tie.")

def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


def handle_turn(player):

  # Set global variables we need to edit
  global winner

  # Get position from player
  print(player + "'s turn.")
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
  board[position] = player

  # Show the game board
  display_board()


# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_for_tie()


def check_for_winner():
    #set up global variable
    global winner

    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    #set up global variable
    global game_still_going
    #chack if any of the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #if any row has a match , flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #return the winner X or O
    if row_1:
       return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any row has a match , flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #return the winner X or O
    if column_1:
       return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None #if there is no winner

def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    # if any row has a match , flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return the winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    else:
        return None


def check_for_tie():
  # Set global variables
  global game_still_going
  # If board is full
  if "-" not in board:
    game_still_going = False
    return True
  # Else there is no tie
  else:
    return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player ="O"
    elif current_player == "O":
        current_player = "X"


#--Start----

play_game()