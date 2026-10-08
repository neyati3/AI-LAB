import heapq
GOAL = (1, 2, 3,
        8, 0, 4,
        7, 6, 5)
def manhattan_distance(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile != 0:
            goal_index = GOAL.index(tile)
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)
    return distance
def get_neighbors(state):
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))
    return neighbors
def a_star(start):
    priority_queue = []
    g = 0
    h = manhattan_distance(start)
    f = g + h
    heapq.heappush(priority_queue, (f, g, start, [start]))
    visited = set()
    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)
        if current == GOAL:
            return path
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_h = manhattan_distance(neighbor)
                new_f = new_g + new_h
                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )
    return None
def print_puzzle(state):
    print("+---+---+---+")
    for i in range(0, 9, 3):
        print("|", state[i], "|", state[i+1], "|", state[i+2], "|")
        print("+---+---+---+")
print("Enter the 8-puzzle start state.")
print("Use 0 for the blank space.")
print("Example: 1 2 3 4 0 6 7 5 8")
values = list(map(int, input("Enter 9 numbers: ").split()))
if len(values) != 9 or set(values) != set(range(9)):
    print("Invalid input!")
    print("Please enter numbers 0 to 8 exactly once.")
    exit()
start = tuple(values)
print("\nStart State:")
print_puzzle(start)
solution = a_star(start)
if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)
    print("\nSteps:\n")
    for step, state in enumerate(solution):
        print("Step", step)
        print_puzzle(state)
else:
    print("No solution exists.")
