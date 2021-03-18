#### TIC TAC TOE ###
import getpass
#createboard
board = ["-","-","-","-","-","-","-","-","-",]
#first player
player = "X"
game_on = True
#No winner at the beginning
winner = None
print("Tic-Tac-Toe")

display_board = lambda: print(' --- --- --- \n'.join([f'| {board[(i*3)]} | {board[(i*3)+1]} | {board[(i*3)+2]} |\n' for i in range(2, -1, -1)]))

#method to play the game
def play_game():
  display_board()
  
  while game_on:
    
    handle_turn(player)
    
    game_over()
    
    flip_player()

  if winner=="X" or winner=="O":
    print(f"Yipeeee!!! {winner} WON.")
  elif not winner:
    print("Its a Tie") 
  
#handleuser
def handle_turn(player):
  print(f"{player}'s turn")
  position = getpass.getpass("Choose the position: ")
  valid = False

  while not valid:
    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = getpass.getpass("Choose the position: ")

    position = int(position) -1

    if board[position] == "-":
      valid = True
    else:
      print("Oops You can't go there")  



  board[position] = player
  display_board()
  
def flip_player():
  global player 
  
  if player == "X":
    player = "O"
  elif player == "O":
    player = "X"
  
  return
    
def game_over():
  
  check_win()
  
  check_tie()
#checkwin
def check_win():
  
  global winner 

  row_winner=row_win()
  
  column_winner=column_win()
  
  diagonal_winner=diagonal_win()

  if row_winner:
    winner=row_win()

  elif column_winner:
    winner=column_win()

  elif diagonal_winner:
     winner=diagonal_win()

  else:
    winner=None     
  
def row_win():
  global game_on
  row1 = board[6]==board[7]==board[8]!="-"
  row2 = board[3]==board[4]==board[5]!="-"
  row3 = board[0]==board[1]==board[2]!="-"

  if row1 or row2 or row3:
    game_on = False

  if row1:
    return board[6]
  elif row2:
    return board[3]
  elif row3:
    return board[0]

  return

def column_win():

  global game_on
  col1 = board[6]==board[3]==board[0]!="-"
  col2 = board[7]==board[4]==board[1]!="-"
  col3 = board[8]==board[5]==board[2]!="-"
  
  if col1 or col2 or col3:
    game_on = False

  if col1:
    return board[6]
  elif col2:
    return board[7]
  elif col3:
    return board[8]    

def diagonal_win():

  global game_on
  dia1 = board[6]==board[4]==board[2]!="-"
  dia2 = board[8]==board[4]==board[0]!="-"
  
  if dia1 or dia2:
    game_on = False

  if dia1:
    return board[6]
  elif dia2:
    return board[8]  

#checktie
def check_tie():

  global game_on
  if "-" not in board:
    game_on=False
  
play_game()

 
