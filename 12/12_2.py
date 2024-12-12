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

directions = [(-1, 0, 'UP'), (0, 1, 'RIGHT'), (1, 0, 'DOWN'), (0, -1, 'LEFT')]

for i in range(rows):
    for j in range(cols):
        if not visited[i][j]:
            plant_type = grid[i][j]
            stack = [(i, j)]
            visited[i][j] = True
            area = 0
            perimeter_edges = []
            while stack:
                x, y = stack.pop()
                area += 1
                for dx, dy, direction in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if grid[nx][ny] == plant_type:
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                        else:
                            perimeter_edges.append((x, y, direction))
                    else:
                        perimeter_edges.append((x, y, direction))
            edges_by_direction = {'UP': {}, 'DOWN': {}, 'LEFT': {}, 'RIGHT': {}}

            for x, y, direction in perimeter_edges:
                if direction == 'UP' or direction == 'DOWN':
                    x_key = x
                    y_set = edges_by_direction[direction].setdefault(x_key, set())
                    y_set.add(y)
                else:  # 'LEFT' or 'RIGHT'
                    y_key = y
                    x_set = edges_by_direction[direction].setdefault(y_key, set())
                    x_set.add(x)

            sides = 0

            for direction in ['UP', 'DOWN']:
                for x_key, y_positions in edges_by_direction[direction].items():
                    y_list = sorted(y_positions)
                    prev_y = None
                    for y in y_list:
                        if prev_y is None or y != prev_y + 1:
                            sides += 1
                        prev_y = y

            for direction in ['LEFT', 'RIGHT']:
                for y_key, x_positions in edges_by_direction[direction].items():
                    x_list = sorted(x_positions)
                    prev_x = None
                    for x in x_list:
                        if prev_x is None or x != prev_x + 1:
                            sides += 1
                        prev_x = x

            total_price += area * sides

print(total_price)