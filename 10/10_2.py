with open("input (9).txt", 'r') as file:
    input_data = file.read().splitlines()

map_ = [[int(c) for c in row] for row in input_data]
rows = len(map_)
cols = len(map_[0])

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
total = 0

for y in range(rows):
    for x in range(cols):
        if map_[y][x] == 0:
            visited = []
            stack = [(x, y, 1)]
            while stack:
                cx, cy, search = stack.pop()
                for dx, dy in directions:
                    xx, yy = cx + dx, cy + dy
                    if 0 <= xx < cols and 0 <= yy < rows and map_[yy][xx] == search:
                        if search == 9:
                            visited.append((xx, yy))
                        else:
                            stack.append((xx, yy, search + 1))
            total += len(visited)

print(total)