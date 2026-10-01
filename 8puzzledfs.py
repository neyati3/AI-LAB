GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_pos] = \
                new_state[new_pos], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors
def dfs(start):
    stack = [start]
    visited = set()
    parent = {start: None}
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                if neighbor not in parent:
                    parent[neighbor] = current
                stack.append(neighbor)
    return None
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()
start = tuple(map(int, input(
    "Enter initial state (use 0 for blank): "
).split()))
if len(start) != 9:
    print("Invalid input!")
else:
    solution = dfs(start)
    if solution is None:
        print("No solution exists.")
    else:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)
        print("\nSteps:")
        for i, state in enumerate(solution):
            print("Step", i)
            print_puzzle(state)
