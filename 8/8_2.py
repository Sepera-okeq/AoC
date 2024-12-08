import math

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

    def calc_t_range(a, step, lower_bound, upper_bound):
        if step > 0:
            t_min = (lower_bound - a) / step
            t_max = (upper_bound - a) / step
        elif step < 0:
            t_min = (upper_bound - a) / step
            t_max = (lower_bound - a) / step
        else:  # step == 0
            if lower_bound <= a <= upper_bound:
                t_min = -math.inf
                t_max = math.inf
            else:
                t_min = math.inf
                t_max = -math.inf
        return t_min, t_max

    for freq, positions in antennas.items():
        n = len(positions)
        if n < 2:
            continue
        for pos in positions:
            antinodes.add(pos)

        for i in range(n):
            for j in range(i + 1, n):
                A1 = positions[i]
                A2 = positions[j]

                dx = A2[0] - A1[0]
                dy = A2[1] - A1[1]
                gcd = math.gcd(dx, dy)
                if gcd == 0:
                    antinodes.add(A1)
                    continue
                step_x = dx // gcd
                step_y = dy // gcd

                t_min_x, t_max_x = calc_t_range(A1[0], step_x, 0, cols - 1)
                t_min_y, t_max_y = calc_t_range(A1[1], step_y, 0, rows - 1)
                t_start = max(t_min_x, t_min_y)
                t_end = min(t_max_x, t_max_y)
                t_start = math.ceil(t_start)
                t_end = math.floor(t_end)
                if t_start > t_end:
                    continue

                for t in range(int(t_start), int(t_end) + 1):
                    x = A1[0] + t * step_x
                    y = A1[1] + t * step_y
                    if 0 <= x < cols and 0 <= y < rows:
                        antinodes.add((x, y))

    result = len(antinodes)
    return result


print(fuck_solver_son_suka("input (7).txt"))