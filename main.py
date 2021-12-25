# --------- Global Variables -----------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
game_still_going = True

# Lets us know who the current player is (X always goes first)
current_player = "X"

# Lets us know who the winner is
winner = None


# ------------- Functions ---------------


# Display the current board
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")


# Handle each turn
def handle_turn(player):

  # Getting position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, making sure it is a valid input and also that the spot is open
  valid = False
  while not valid:

    # Making sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
 
    # Getting correct index for the board 
    position = int(position) - 1

    # Making sure the spot is available on the board
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # Putting the game piece on the board
  board[position] = player

  # Showing the game board
  display_board()


# Checking if the game ends
def check_if_game_over():
  check_for_winner()
  check_for_tie()


# Checking if somebody won
def check_for_winner():

  # Set global variables
  global winner

  # Checking if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


# Check the rows for a win
def check_rows():

  # Set global variables
  global game_still_going

  # Checking if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False

  # Return the winner
  if row_1:
    return board[0] 
  elif row_2:
    return board[3] 
  elif row_3:
    return board[6] 

  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():

  # Set global variables
  global game_still_going

  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  # If any row does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False

  # Return the winner
  if column_1:
    return board[0] 
  elif column_2:
    return board[1] 
  elif column_3:
    return board[2] 

  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():

  # Set global variables
  global game_still_going

  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  # If any row does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False

  # Return the winner
  if diagonal_1:
    return board[0] 
  elif diagonal_2:
    return board[2]

  # Or return None if there was no winner
  else:
    return None


# Checking if there is a tie
def check_for_tie():

  # Set global variables
  global game_still_going

  # if board is full
  if "-" not in board:
    game_still_going = False
    return True

  # else there is no tie
  else:
    return False


# Flip the current player from X to O, or O to X
def flip_player():

  # Global variables we need
  global current_player

  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"

  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"


#  Cleaning the board and players to replay the game from start
def clear_board():

  # Set global variables
  global board, current_player, winner, game_still_going

  # Setting the default values
  board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
  current_player = "X"
  game_still_going = True
  winner = None


# main game
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
  
  # Since the game is over, printing the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")


# Main funtion which runs at the start
def main_game():
  # Initialize a variable to check if player is still wanting to play
  replay = "Y"  
  # Make a loop for replaying
  while replay=="Y":
    # Clear the board before every match
    clear_board()
    # Send the player to each match
    play_game()
    # Asking player if they want to continue
    replay = input("Do you want to play again? Enter Y to continue playing and anything else to quit: ")
  # Printing a text message to show player that they decided to quit.
  print("Thank you for playing.")


# ------------ Start Execution -------------

# Play a game of tic tac toe
main_game()