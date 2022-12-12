#Создайте программу для игры в ""Крестики-нолики"".
#немного не разобралась...делала с мануалом(

board = [1,2,3,
        4,5,6,
        7,8,9]

victories = [[0, 1, 2], # Выигрышные комбинации
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_board():
    print(board[0], end=" ")
    print(board[1], end=" ")
    print(board[2])

    print(board[3], end=" ")
    print(board[4], end=" ")
    print(board[5])

    print(board[6], end=" ")
    print(board[7], end=" ")
    print(board[8])

#player_1 = input('Игрок 1 (ник): ')
#player_2 = input('Игрок 2 (ник): ')
#start_player = randint(1, 2)
#if start_player == 1:
#    print(f'Первым ходит {player_1} ')
#else:
#   print(f'Первым ходит {player_2} ')

def step_board(step,symbol):
    ind = board.index(step)
    board[ind] = symbol

def get_result():
    win = ""

    for i in victories:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win = "O"

    return win

game_over = False
player_1 = True

while game_over == False:

    print_board()

    if player_1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Инрок 2, ваш ход: "))

    step_board(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player_1 = not (player_1)

print_board()
print("Победил", win)