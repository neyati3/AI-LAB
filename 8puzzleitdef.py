
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
def depth_limited_dfs(state, depth, visited, path):
    if state == GOAL:
        return path
    if depth == 0:
        return None
    visited.add(state)
    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_dfs(
                neighbor,
                depth - 1,
                visited,
                path + [neighbor]
            )
            if result is not None:
                return result
    visited.remove(state)
    return None
def dfs(start):
    for depth in range(50):
        visited = set()
        result = depth_limited_dfs(
            start,
            depth,
            visited,
            [start]
        )
        if result is not None:
            return result
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
