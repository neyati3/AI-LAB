import math
board = [' ' for _ in range(9)]
def print_board(b):
    print("\n")
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("-----------")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("-----------")
    print(f" {b[6]} | {b[7]} | {b[8]} ")
    print("\n")
def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)
def is_full(b):
    return ' ' not in b
def get_empty_cells(b):
    return [i for i, spot in enumerate(b) if spot == ' ']
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 10 - depth
    if check_winner(b, 'X'):
        return depth - 10
    if is_full(b):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for move in get_empty_cells(b):
            b[move] = 'O'
            score = minimax(b, depth + 1, False)
            b[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_empty_cells(b):
            b[move] = 'X'
            score = minimax(b, depth + 1, True)
            b[move] = ' '
            best_score = min(score, best_score)
        return best_score
def ai_move(b):
    best_score = -math.inf
    move = None
    for cell in get_empty_cells(b):
        b[cell] = 'O'
        score = minimax(b, 0, False)
        b[cell] = ' '
        if score > best_score:
            best_score = score
            move = cell
    b[move] = 'O'
def play_game():
    global board
    board = [' ' for _ in range(9)]
    print("Welcome to Tic-Tac-Toe! You are 'X' and the Computer is 'O'.")
    print("Positions are numbered from 0 to 8 like this:")
    print_board([str(i) for i in range(9)])
    while True:
        try:
            choice = int(input("Enter your move (0-8): "))
            if board[choice] != ' ':
                print("Spot taken! Choose another.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 0 and 8.")
            continue
        board[choice] = 'X'
        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations, you win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        print("Computer ('O') is thinking...")
        ai_move(board)
        if check_winner(board, 'O'):
            print_board(board)
            print("Computer wins! Better luck next time.")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        print_board(board)
play_game()
