from collections import deque

with open("input (17).txt", "r") as file:
    data = file.read().splitlines()
data = [tuple(map(int, line.split(','))) for line in data]

grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
for step, (x, y) in enumerate(data[:1024]):
    grid[y][x] = '#'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
start = (0, 0)
end = (70, 70)
queue = [(start, 0)]
visited = set()
visited.add(start)

while queue:
    current, steps = queue.pop(0)
    if current == end:
        print(steps)
        break
    for dx, dy in directions:
        nx, ny = current[0] + dx, current[1] + dy
        if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[ny][nx] == '.' and (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append(((nx, ny), steps + 1))