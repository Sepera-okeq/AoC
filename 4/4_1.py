with open('input (3).txt', 'r', encoding='utf-8') as file:
    data = [list(line.strip()) for line in file]

def count_xmas(grid):
    directions = [
        (0, 1),    # Вправо
        (0, -1),   # Влево
        (1, 0),    # Вниз
        (-1, 0),   # Вверх
        (1, 1),    # Диагональ вниз-вправо
        (-1, -1),  # Диагональ вверх-влево
        (1, -1),   # Диагональ вниз-влево
        (-1, 1)    # Диагональ вверх-вправо
    ]

    target = "XMAS"
    count = 0

    for x in range(len(grid)):                  # Для каждой строки
        for y in range(len(grid[0])):           # Для каждого символа в строке
            for dx, dy in directions:
                match = True
                for k in range(len(target)):
                    nx, ny = x + k * dx, y + k * dy
                    if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != target[k]:
                        match = False
                        break
                if match:
                    count += 1

    return count

print(count_xmas(data))