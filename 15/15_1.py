with open("input (14).txt", "r") as file:
    file_content = file.read()

grid_lines, commands = file_content.strip().split("\n\n")
grid = [list(line) for line in grid_lines.split("\n")]

grid_data = [row[:] for row in grid]

i, j = next(
    (i, j)
    for i in range(len(grid_data))
    for j in range(len(grid_data[0]))
    if grid_data[i][j] == '@'
)

for command in commands:
    if command == "<":
        di, dj = 0, -1
    elif command == ">":
        di, dj = 0, 1
    elif command == "^":
        di, dj = -1, 0
    elif command == "v":
        di, dj = 1, 0

    ni, nj = i + di, j + dj
    while (
        0 <= ni < len(grid_data)
        and 0 <= nj < len(grid_data[0])
        and grid_data[ni][nj] == "O"
    ):
        ni += di
        nj += dj
    if (
        0 <= ni < len(grid_data)
        and 0 <= nj < len(grid_data[0])
        and grid_data[ni][nj] == "."
    ):
        grid_data[ni][nj] = "O"
        grid_data[i + di][j + dj] = "@"
        grid_data[i][j] = "."
        i, j = i + di, j + dj

print(
    sum(
        i * 100 + j
        for i in range(len(grid_data))
        for j in range(len(grid_data[0]))
        if grid_data[i][j] in ("O", "[")
    )
)
