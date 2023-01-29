board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def print_board():
    for row in board:
        print(' '.join(row))

def check_winner():
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] != ' ':
                return board[0][col]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != ' ':
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] != ' ':
            return board[0][2]
    return None

player = 'X'

while True:
    print_board()
    move = input("Enter row, col for " + player + " (e.g. 0,1): ")
    row, col = move.split(',')
    row, col = int(row), int(col)
    if board[row][col] != ' ':
        print("That space is already occupied! Try again.")
        continue
    board[row][col] = player
    winner = check_winner()
    if winner:
        print(winner + " wins!")
        break
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
