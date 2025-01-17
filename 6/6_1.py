def parse_input(file_path):
    with open(file_path, "r") as f:
        grid = f.read().strip().split("\n")
    
    guard_position = None
    guard_direction = None
    obstacles = set()
    
    # Направления: ^ (вверх), > (вправо), v (вниз), < (влево)
    dir_map = {"^": 0, ">": 1, "v": 2, "<": 3}
    
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in dir_map.keys():
                guard_position = (x, y)
                guard_direction = dir_map[cell]
            elif cell == "#":
                obstacles.add((x, y))
    
    return grid, guard_position, guard_direction, obstacles


def simulate_patrol(grid, start_position, start_direction, obstacles):
    max_x = len(grid[0])
    max_y = len(grid)
    
    # Сдвиги для направлений: Вверх, Вправо, Вниз, Влево
    deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    
    visited_states = set()
    position = start_position
    direction = start_direction
    
    while True:
        visited_states.add(position)
        
        dx, dy = deltas[direction]
        next_position = (position[0] + dx, position[1] + dy)
        
        if not (0 <= next_position[0] < max_x and 0 <= next_position[1] < max_y):
            break
        
        if next_position in obstacles:
            direction = (direction + 1) % 4
        else:
            position = next_position
    
    return len(visited_states)


grid, start_position, start_direction, obstacles = parse_input("input (5).txt")
print(simulate_patrol(grid, start_position, start_direction, obstacles))