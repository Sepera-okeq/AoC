with open('input (3).txt', 'r', encoding='utf-8') as file:
    data = [list(line.strip()) for line in file]

def count_x_mas(grid):
    count = 0

    for x in range(1, len(grid) - 1):                  # Проход по всем строкам, кроме первой и последней
        for y in range(1, len(grid[0]) - 1):           # Проход по всем столбцам, кроме первого и последнего
            if grid[x][y] == 'A':
                a = grid[x - 1][y - 1] + grid[x][y] + grid[x + 1][y + 1]
                b = grid[x + 1][y - 1] + grid[x][y] + grid[x - 1][y + 1]

                if (a == "MAS" or a == "SAM") and (b == "MAS" or b == "SAM"):
                    count += 1
    return count

print(count_x_mas(data))