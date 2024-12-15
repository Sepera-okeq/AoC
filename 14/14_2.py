robots = []
width = 101
height = 103

with open('input (13).txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.strip().split()
        p_part = parts[0]
        v_part = parts[1]
        x_pos, y_pos = map(int, p_part[2:].split(','))
        x_vel, y_vel = map(int, v_part[2:].split(','))
        robots.append([x_pos, y_pos, x_vel, y_vel])

def update_positions(robots, t):
    positions = []
    for robot in robots:
        x0, y0, dx, dy = robot
        x = (x0 + dx * t) % width
        y = (y0 + dy * t) % height
        positions.append((x, y))
    return positions

def find_min_area_time(robots):
    min_area = None
    min_time = None
    min_positions = None
    t = 0
    max_time = 20000
    while t < max_time:
        positions = update_positions(robots, t)
        xs = [x for x, y in positions]
        ys = [y for x, y in positions]
        width_area = max(xs) - min(xs) + 1
        height_area = max(ys) - min(ys) + 1
        area = width_area * height_area

        grid = {}
        for x, y in positions:
            grid[(x, y)] = '#'

        has_line = False
        for y in range(min(ys), max(ys)+1):
            count = 0
            for x in range(min(xs), max(xs)+1):
                if (x, y) in grid:
                    count += 1
                else:
                    count = 0
                if count >= 14:
                    has_line = True
                    break
            if has_line:
                break

        for x in range(min(xs), max(xs)+1):
            count = 0
            for y in range(min(ys), max(ys)+1):
                if (x, y) in grid:
                    count += 1
                else:
                    count = 0
                if count >= 14:
                    has_line = True
                    break
            if has_line:
                break

        if has_line:
            min_area = area
            min_time = t
            min_positions = positions
            break

        t += 1

    return min_time, min_positions

min_time, min_positions = find_min_area_time(robots)

if min_time is not None:
    print(f"min sec: {min_time}")

    xs = [x for x, y in min_positions]
    ys = [y for x, y in min_positions]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    grid = [['.' for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]

    for x, y in min_positions:
        grid[y - min_y][x - min_x] = '#'

    print("pos robots {}:".format(min_time))
    for row in grid:
        print(''.join(row))

else:
    print("no found.")