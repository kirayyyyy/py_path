board = [
    ["","",""],
    ["","",""],
    ["","",""]
]
def show_board():
        for row in board:
            print(f"{row[0]} | {row[1]} | {row[2]}")
            print("----------")
def place_mark(player):
        while True:
            row= int(input("Row (0-2):"))
            col = int(input("Column (0-2):"))
            if board[row][col] == "":
                board[row][col] = player
                break
            else:
                print("That square is already taken!")
def check_win(player):
            for i in range(3):
                if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                     return True
            for x in range(3):
                  if board[0][x] == player and board[1][x] == player and board[2][x] == player:
                    return True
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            if board[2][0] == player and board[1][1] == player and board[0][2] == player:
                return True
            return False
turn = 0
current_player = "X"
while turn != 9:
    show_board()
    place_mark(current_player)
    if check_win(current_player):
                show_board()
                print(current_player,"Wins!")
                break
    if current_player == "X":
            current_player = "O"
    else:
          current_player = "X"
    turn += 1
print("It's a draw!")