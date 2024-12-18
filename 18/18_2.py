from collections import deque

with open("input (17).txt", "r") as file:
    data = file.read().splitlines()
data = [tuple(map(int, line.split(','))) for line in data]

grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_path_possible():
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    while queue:
        x, y = queue.popleft()
        if (x, y) == (70, 70):
            return True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False

for step, (x, y) in enumerate(data):
    grid[y][x] = '#'
    if not is_path_possible():
        print(f"{x},{y}")
        break