import sys
import heapq

maze = []
with open('input (15).txt', 'r') as file:
    for line in file:
        maze.append(list(line.rstrip('\n')))

rows = len(maze)
cols = len(maze[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction_names = ['N', 'E', 'S', 'W']

for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 'S':
            start_pos = (i, j)
        if maze[i][j] == 'E':
            end_pos = (i, j)

heap = []
start_state = (0, start_pos[0], start_pos[1], 1)
heapq.heappush(heap, start_state)

cost = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]
cost[start_pos[0]][start_pos[1]][1] = 0

while heap:
    c, x, y, dir = heapq.heappop(heap)

    if (x, y) == end_pos:
        pass

    if c > cost[x][y][dir]:
        continue

    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
        if cost[nx][ny][dir] > c + 1:
            cost[nx][ny][dir] = c + 1
            heapq.heappush(heap, (c + 1, nx, ny, dir))

    new_dir = (dir - 1) % 4
    if cost[x][y][new_dir] > c + 1000:
        cost[x][y][new_dir] = c + 1000
        heapq.heappush(heap, (c + 1000, x, y, new_dir))

    new_dir = (dir + 1) % 4
    if cost[x][y][new_dir] > c + 1000:
        cost[x][y][new_dir] = c + 1000
        heapq.heappush(heap, (c + 1000, x, y, new_dir))

min_cost = float('inf')
for dir in range(4):
    if cost[end_pos[0]][end_pos[1]][dir] < min_cost:
        min_cost = cost[end_pos[0]][end_pos[1]][dir]

from collections import deque

queue = deque()
positions_on_minimal_paths = set()

for dir in range(4):
    if cost[end_pos[0]][end_pos[1]][dir] == min_cost:
        queue.append((end_pos[0], end_pos[1], dir))

visited = [[[False]*4 for _ in range(cols)] for _ in range(rows)]

while queue:
    x, y, dir = queue.popleft()
    if visited[x][y][dir]:
        continue
    visited[x][y][dir] = True
    positions_on_minimal_paths.add((x, y))

    current_cost = cost[x][y][dir]

    dx, dy = directions[dir]
    prev_x, prev_y = x - dx, y - dy
    if 0 <= prev_x < rows and 0 <= prev_y < cols and maze[prev_x][prev_y] != '#':
        if cost[prev_x][prev_y][dir] == current_cost - 1:
            queue.append((prev_x, prev_y, dir))

    prev_dir = (dir + 1) % 4
    if cost[x][y][prev_dir] == current_cost - 1000:
        queue.append((x, y, prev_dir))

    prev_dir = (dir - 1) % 4
    if cost[x][y][prev_dir] == current_cost - 1000:
        queue.append((x, y, prev_dir))

print(len(positions_on_minimal_paths))