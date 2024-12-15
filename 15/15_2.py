with open("input (14).txt", "r") as file:
    file_content = file.read()

grid_lines, commands = file_content.strip().split("\n\n")
grid = [list(line) for line in grid_lines.split("\n")]

grid_data = [
    [
        c
        for char in row
        for c in (
            ["#", "#"]
            if char == '#'
            else (
                ["[", "]"]
                if char == 'O'
                else (
                    [".", "."]
                    if char == '.'
                    else ["@", "."] if char == '@' else []
                )
            )
        )
    ]
    for row in grid
]

i, j = next(
    (i, j)
    for i in range(len(grid_data))
    for j in range(len(grid_data[0]))
    if grid_data[i][j] == '@'
)

for command in commands:
    if command == "<":
        nj = j - 1
        while 0 <= nj < len(grid_data[0]) and grid_data[i][nj] in ('[', ']'):
            nj -= 1
        if 0 <= nj < len(grid_data[0]) and grid_data[i][nj] == '.':
            grid_data[i][nj] = grid_data[i][j - 1]
            grid_data[i][j - 1] = "@"
            grid_data[i][j] = '.'
            for k in range(j - 2, nj - 1, -1):
                grid_data[i][k] = (
                    ']'
                    if grid_data[i][k] == '['
                    else '[' if grid_data[i][k] == ']' else grid_data[i][k]
                )
            j = j - 1
    elif command == ">":
        nj = j + 1
        while 0 <= nj < len(grid_data[0]) and grid_data[i][nj] in ('[', ']'):
            nj += 1
        if 0 <= nj < len(grid_data[0]) and grid_data[i][nj] == '.':
            grid_data[i][nj] = grid_data[i][j + 1]
            grid_data[i][j + 1] = "@"
            grid_data[i][j] = '.'
            for k in range(j + 2, nj + 1):
                grid_data[i][k] = (
                    ']'
                    if grid_data[i][k] == '['
                    else '[' if grid_data[i][k] == ']' else grid_data[i][k]
                )
            j = j + 1
    elif command in ('^', 'v'):
        di = -1 if command == '^' else 1
        cache = {}

        def is_movable(ci, cj, cdi, cache):
            if (ci, cj) in cache:
                return cache[(ci, cj)]
            if grid_data[ci][cj] == '@':
                if (
                    0 <= ci + cdi < len(grid_data)
                    and 0 <= cj < len(grid_data[0])
                    and grid_data[ci + cdi][cj] == '.'
                ):
                    cache[(ci, cj)] = True
                    return True
                elif (
                    0 <= ci + cdi < len(grid_data)
                    and 0 <= cj < len(grid_data[0])
                    and grid_data[ci + cdi][cj] == '['
                ):
                    cache[(ci, cj)] = is_movable(ci + cdi, cj, cdi, cache)
                    return cache[(ci, cj)]
                elif (
                    0 <= ci + cdi < len(grid_data)
                    and 0 <= cj - 1 < len(grid_data[0])
                    and grid_data[ci + cdi][cj] == ']'
                ):
                    cache[(ci, cj)] = is_movable(ci + cdi, cj - 1, cdi, cache)
                    return cache[(ci, cj)]
                else:
                    cache[(ci, cj)] = False
                    return False
            elif grid_data[ci][cj] == '[':
                left = (
                    0 <= ci + cdi < len(grid_data)
                    and 0 <= cj < len(grid_data[0])
                    and grid_data[ci + cdi][cj] == '.'
                    or (
                        0 <= ci + cdi < len(grid_data)
                        and 0 <= cj < len(grid_data[0])
                        and grid_data[ci + cdi][cj] == '['
                        and is_movable(ci + cdi, cj, cdi, cache)
                    )
                    or (
                        0 <= ci + cdi < len(grid_data)
                        and 0 <= cj - 1 < len(grid_data[0])
                        and grid_data[ci + cdi][cj] == ']'
                        and is_movable(ci + cdi, cj - 1, cdi, cache)
                    )
                )
                right = (
                    0 <= ci + cdi < len(grid_data)
                    and 0 <= cj + 1 < len(grid_data[0])
                    and (
                        grid_data[ci + cdi][cj + 1] == '.'
                        or grid_data[ci + cdi][cj + 1] == ']'
                        or (
                            grid_data[ci + cdi][cj + 1] == '['
                            and is_movable(ci + cdi, cj + 1, cdi, cache)
                        )
                    )
                )
                cache[(ci, cj)] = left and right
                return cache[(ci, cj)]

        if is_movable(i, j, di, cache):
            sorted_points = sorted(cache.keys())
            if di > 0:
                sorted_points.reverse()
            for ci, cj in sorted_points:
                if grid_data[ci][cj] == '@':
                    grid_data[ci + di][cj] = '@'
                    grid_data[ci][cj] = '.'
                elif grid_data[ci][cj] == '[':
                    grid_data[ci + di][cj] = '['
                    grid_data[ci + di][cj + 1] = ']'
                    grid_data[ci][cj] = '.'
                    grid_data[ci][cj + 1] = '.'
            i += di

print(
    sum(
        i * 100 + j
        for i in range(len(grid_data))
        for j in range(len(grid_data[0]))
        if grid_data[i][j] in ('[',)
    )
)
