def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])  # Always 3 based on problem description
    target_temps = list(map(int, data[1:N]))
    final_positions = list(map(int, data[N:2*N]))
    
    # Setup initial conditions
    initial_temp = 100
    containers = [initial_temp, initial_temp, 0]  # Two containers of 100°C water and one empty
    moves = []
    
    # We need to find a way to move water such that the end temperatures in final_positions match target_temps
    # Mapping from container to final position (1-based index)
    pos_to_container = {}
    for i, pos in enumerate(final_positions):
        if pos > 0:
            pos_to_container[pos] = i + 1
    
    try:
        # Simulate the necessary moves
        for water_id, final_pos in pos_to_container.items():
            target_temp = target_temps[water_id - 1]
            current_pos = water_id  # Initially, water 1 is in container 1, water 2 in container 2, etc.
            
            if containers[current_pos - 1] == target_temp:
                if current_pos == final_pos:
                    continue  # Already at the right temp and position
                # Move directly to final position if empty
                if containers[final_pos - 1] == 0:
                    moves.append((current_pos, final_pos))
                    containers[final_pos - 1] = containers[current_pos - 1]
                    containers[current_pos - 1] = 0
                else:
                    raise Exception("Invalid move configuration")
            else:
                # Calculate required transfers to reach the target temperature
                required_moves = (containers[current_pos - 1] - target_temp) // 5
                for _ in range(required_moves):
                    # Find an empty container to move into
                    empty_container = containers.index(0) + 1
                    if empty_container == current_pos:
                        raise Exception("No valid move found")
                    moves.append((current_pos, empty_container))
                    containers[empty_container - 1] = containers[current_pos - 1] - 5
                    containers[current_pos - 1] = 0
                    current_pos = empty_container

                # Final move to the correct final position if not already there
                if current_pos != final_pos:
                    if containers[final_pos - 1] == 0:
                        moves.append((current_pos, final_pos))
                        containers[final_pos - 1] = containers[current_pos - 1]
                        containers[current_pos - 1] = 0
                    else:
                        raise Exception("Final position not empty")
        
        if len(moves) > 40:
            print(-1)
        else:
            print(len(moves))
            for move in moves:
                print(f"{move[0]} {move[1]}")
    except Exception:
        print(-1)
solve()
# Example Usage
# if you want to use this code, you would have to input the data in the appropriate format when executing.
