import sys
from collections import deque
grid = []
S = None
E = None
with open('input (19).txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        grid.append(list(line))
rows = len(grid)
cols = len(grid[0])
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            S = (i, j)
            grid[i][j] = '.'
        elif grid[i][j] == 'E':
            E = (i, j)
            grid[i][j] = '.'
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist_from_start = {}
queue = deque()
queue.append((S[0], S[1], 0))
dist_from_start[(S[0], S[1])] = 0
while queue:
    x, y, d = queue.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == '.' and (nx, ny) not in dist_from_start:
                dist_from_start[(nx, ny)] = d + 1
                queue.append((nx, ny, d + 1))
dist_to_end = {}
queue = deque()
queue.append((E[0], E[1], 0))
dist_to_end[(E[0], E[1])] = 0
while queue:
    x, y, d = queue.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            if grid[nx][ny] == '.' and (nx, ny) not in dist_to_end:
                dist_to_end[(nx, ny)] = d + 1
                queue.append((nx, ny, d + 1))
if E not in dist_from_start:
    print(0)
    exit()
L = dist_from_start[E]
cheats = set()
count = 0
for x1 in range(rows):
    for y1 in range(cols):
        if grid[x1][y1] != '.':
            continue
        p1 = (x1, y1)
        if p1 not in dist_from_start:
            continue
        L1 = dist_from_start[p1]
        for cheat_cost in [1, 2]:
            if cheat_cost == 1:
                for dx1, dy1 in dirs:
                    x2, y2 = x1 + dx1, y1 + dy1
                    if 0 <= x2 < rows and 0 <= y2 < cols:
                        if grid[x2][y2] == '.':
                            p2 = (x2, y2)
                            if p2 not in dist_to_end:
                                continue
                            L2 = dist_to_end[p2]
                            total_cost = L1 + 1 + L2
                            saved = L - total_cost
                            if saved >= 100:
                                if (p1, p2) not in cheats:
                                    cheats.add((p1, p2))
                                    count += 1
            else:
                for dx1, dy1 in dirs:
                    x_int, y_int = x1 + dx1, y1 + dy1
                    if 0 <= x_int < rows and 0 <= y_int < cols:
                        for dx2, dy2 in dirs:
                            x2, y2 = x_int + dx2, y_int + dy2
                            if 0 <= x2 < rows and 0 <= y2 < cols:
                                if grid[x2][y2] == '.':
                                    p2 = (x2, y2)
                                    if p2 not in dist_to_end:
                                        continue
                                    L2 = dist_to_end[p2]
                                    total_cost = L1 + 2 + L2
                                    saved = L - total_cost
                                    if saved >= 100:
                                        if (p1, p2) not in cheats:
                                            cheats.add((p1, p2))
                                            count += 1
print(count)