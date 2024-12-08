def fuck_solver_son_suka(filename):
    with open(filename, 'r') as f:
        grid = [list(line.rstrip('\n')) for line in f]
    rows = len(grid)
    cols = len(grid[0]) if grid else 0

    antennas = {}  # частота -> список позиций (x, y)
    for y in range(rows):
        for x in range(cols):
            c = grid[y][x]
            if c != '.':
                antennas.setdefault(c, []).append((x, y))

    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                A1 = positions[i]
                A2 = positions[j]

                antinode1_x = 2 * A2[0] - A1[0]
                antinode1_y = 2 * A2[1] - A1[1]

                antinode2_x = 2 * A1[0] - A2[0]
                antinode2_y = 2 * A1[1] - A2[1]

                if 0 <= antinode1_x < cols and 0 <= antinode1_y < rows:
                    antinodes.add((antinode1_x, antinode1_y))
                if 0 <= antinode2_x < cols and 0 <= antinode2_y < rows:
                    antinodes.add((antinode2_x, antinode2_y))

    result = len(antinodes)
    return result


print(fuck_solver_son_suka("input (7).txt"))