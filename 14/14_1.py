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

for robot in robots:
    x, y, dx, dy = robot
    x = (x + dx * 100) % width
    y = (y + dy * 100) % height
    robot[0], robot[1] = x, y

mid_x = (width - 1) / 2.0
mid_y = (height - 1) / 2.0

q1 = q2 = q3 = q4 = 0

for robot in robots:
    x, y = robot[0], robot[1]
    if x == mid_x or y == mid_y:
        continue
    elif x < mid_x and y < mid_y:
        q1 += 1
    elif x > mid_x and y < mid_y:
        q2 += 1
    elif x < mid_x and y > mid_y:
        q3 += 1
    elif x > mid_x and y > mid_y:
        q4 += 1

safety_factor = q1 * q2 * q3 * q4

print(safety_factor)