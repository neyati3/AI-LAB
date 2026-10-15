import random
N = 4
def heuristic(board):
    conflicts = 0
    for i in range(N):
        for j in range(i + 1, N):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts
def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
def hill_climbing():
    board = [random.randint(0, N - 1) for _ in range(N)]
    step = 1
    while True:
        current_h = heuristic(board)
        print("\nStep", step)
        print("Current state:", board)
        print("Heuristic value:", current_h)
        print_board(board)
        if current_h == 0:
            print("Solution found!")
            return board
        best_board = board[:]
        best_h = current_h
        print("\nNeighboring states:")
        for col in range(N):
            for row in range(N):
                if board[col] != row:
                    neighbor = board[:]
                    neighbor[col] = row
                    h = heuristic(neighbor)
                    if h < best_h:
                        best_h = h
                        best_board = neighbor
        if best_h >= current_h:
            print("\nLocal minimum reached!")
            print("Restarting with a new random state...")
            board = [random.randint(0, N - 1) for _ in range(N)]
            print("New random state:", board)
        else:
            board = best_board
            print("\nBest next state:", board)
            print("Best heuristic:", best_h)
        step += 1
solution = hill_climbing()
print("\nFinal Solution:")
print("State:", solution)
print_board(solution)
print("Heuristic value:", heuristic(solution))
