from queue import PriorityQueue
# State representation: (missionaries_left, cannibals_left, boat_position)
initial_state = (3, 3, 1)
goal_state = (0, 0, 0)
def is_valid_state(state):
    missionaries_left, cannibals_left, boat_position = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # Check if missionaries are outnumbered by cannibals on either side
    if (missionaries_left < cannibals_left and missionaries_left > 0) or \
       (missionaries_right < cannibals_right and missionaries_right > 0):
        return False

    return True
def heuristic(state):
    # Heuristic: Number of missionaries and cannibals on the left bank
    return state[0] + state[1]
def generate_next_states(current_state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []
    for move in moves:
        missionaries_left, cannibals_left, boat_position = current_state
        missionaries_move, cannibals_move = move
        # Check if the move is valid
        if boat_position == 1:
            missionaries_left -= missionaries_move
            cannibals_left -= cannibals_move
        else:
            missionaries_left += missionaries_move
            cannibals_left += cannibals_move
        new_state = (missionaries_left, cannibals_left, 1 - boat_position)
        if is_valid_state(new_state):
            next_states.append(new_state)
    # Sort the next states based on the number of people on the right bank
    next_states.sort(key=lambda state: state[0] + state[1])
    return next_states
def a_star_search():
    priority_queue = PriorityQueue()
    visited = set()
    priority_queue.put((0, 0, initial_state, []))
    while not priority_queue.empty():
        _, cost, current_state, path = priority_queue.get()
        if current_state == goal_state:
            return path + [current_state]
        if current_state not in visited:
            visited.add(current_state)
            next_states = generate_next_states(current_state)
            for next_state in next_states:
                priority_queue.put((cost + 1 + heuristic(next_state), cost + 1, next_state, path + [current_state]))
    return None
def print_solution(solution):
    for i, state in enumerate(solution):
        print(f"Step {i + 1}: {state[:2]} Missionaries on the left, {3 - state[0]} Missionaries on the right, "
              f"{state[1]} Cannibals on the left, {3 - state[1]} Cannibals on the right, Boat on {'left' if state[2] == 1 else 'right'}")


solution = a_star_search()
if solution:
  print("Solution found!")
  print_solution(solution)
else:
  print("No solution found.")
