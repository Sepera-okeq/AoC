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
def bfs(start):
    dist = {}
    queue = deque()
    queue.append((start[0], start[1], 0))
    dist[(start[0], start[1])] = 0
    while queue:
        x, y, d = queue.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == '.' and (nx, ny) not in dist:
                    dist[(nx, ny)] = d + 1
                    queue.append((nx, ny, d + 1))
    return dist
dist_from_start = bfs(S)
dist_to_end = bfs(E)
if E not in dist_from_start:
    print("0")
    exit()
L = dist_from_start[E]
cheats = set()
for p1 in dist_from_start:
    L1 = dist_from_start[p1]
    queue = deque()
    queue.append((p1[0], p1[1], 0))
    visited = {}
    visited[(p1[0], p1[1])] = 0
    while queue:
        x, y, cheat_cost = queue.popleft()
        if cheat_cost > 20:
            continue
        if grid[x][y] == '.' and (x, y) != p1:
            p2 = (x, y)
            if p2 in dist_to_end:
                L2 = dist_to_end[p2]
                total_cost = L1 + cheat_cost + L2
                saved = L - total_cost
                if saved >= 100:
                    if (p1, p2) not in cheats:
                        cheats.add((p1, p2))
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            n_cheat_cost = cheat_cost + 1
            if n_cheat_cost > 20:
                continue
            if 0 <= nx < rows and 0 <= ny < cols:
                if ((nx, ny) not in visited) or (visited[(nx, ny)] > n_cheat_cost):
                    visited[(nx, ny)] = n_cheat_cost
                    queue.append((nx, ny, n_cheat_cost))
print(len(cheats))