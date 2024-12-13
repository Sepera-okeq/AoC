with open("input (12).txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

machines = []
for i in range(0, len(lines), 3):
    line1, line2, line3 = lines[i], lines[i + 1], lines[i + 2]

    idx_xa = line1.find("X+") + 2
    idx_ya = line1.find("Y+") + 2
    ax = int(line1[idx_xa:line1.find(",", idx_xa)])
    ay = int(line1[idx_ya:])

    idx_xb = line2.find("X+") + 2
    idx_yb = line2.find("Y+") + 2
    bx = int(line2[idx_xb:line2.find(",", idx_xb)])
    by = int(line2[idx_yb:])

    idx_x0 = line3.find("X=") + 2
    idx_y0 = line3.find("Y=") + 2
    x0 = int(line3[idx_x0:line3.find(",", idx_x0)])
    y0 = int(line3[idx_y0:])

    machines.append(((ax, ay), (bx, by), (x0, y0)))

total_cost = 0

for (ax, ay), (bx, by), (x0, y0) in machines:
    denominator = ax * by - ay * bx
    if denominator == 0:
        continue

    b = (ax * y0 - ay * x0) / denominator
    a = (x0 - bx * b) / ax if ax != 0 else (y0 - by * b) / ay

    if a.is_integer() and b.is_integer() and 0 <= a <= 100 and 0 <= b <= 100:
        a, b = int(a), int(b)
        total_cost += 3 * a + b

print(total_cost)