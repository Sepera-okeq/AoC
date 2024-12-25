lines = open("input (24).txt").read().split("\n\n")

locks = []
keys = []

for line in lines:
    sub_grid = line.splitlines()
    if any(sub_grid[0][k] == "#" for k in range(len(sub_grid[0]))):
        lock = []
        for column in range(len(sub_grid[0])):
            for row in range(len(sub_grid)):
                if sub_grid[row][column] == ".":
                    lock.append(row - 1)
                    break
        locks.append(lock)
    else:
        key = []
        for column in range(len(sub_grid[0])):
            for row in range(len(sub_grid) - 1, -1, -1):
                if sub_grid[row][column] == ".":
                    key.append(len(sub_grid) - row - 2)
                    break
        keys.append(key)

print(sum(all(key[i] + lock[i] <= 5 for i in range(5)) for lock in locks for key in keys))
print("Merry Christmas!")