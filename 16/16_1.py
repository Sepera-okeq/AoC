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
heapq.heappush(heap, (0, start_pos[0], start_pos[1], 1))

visited = {}

while heap:
    cost, x, y, dir = heapq.heappop(heap)
    if (x, y, dir) in visited and visited[(x, y, dir)] <= cost:
        continue
    visited[(x, y, dir)] = cost

    if (x, y) == end_pos:
        print(cost)
        sys.exit()

    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
        heapq.heappush(heap, (cost + 1, nx, ny, dir))

    new_dir = (dir - 1) % 4
    heapq.heappush(heap, (cost + 1000, x, y, new_dir))

    new_dir = (dir + 1) % 4
    heapq.heappush(heap, (cost + 1000, x, y, new_dir))