grid = []
with open('input (11).txt', 'r') as f:
    for line in f:
        line = line.rstrip('\n')
        if line:
            grid.append(list(line))

rows = len(grid)
cols = len(grid[0])

visited = [[False for _ in range(cols)] for _ in range(rows)]
total_price = 0

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            plant_type = grid[i][j]
            stack = [(i, j)]
            visited[i][j] = True
            area = 0
            perimeter = 0
            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == plant_type:
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                        else:
                            perimeter += 1
                    else:
                        perimeter += 1
            total_price += area * perimeter

print(total_price)