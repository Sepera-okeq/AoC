def read_data(file_path):
    column1 = []
    column2 = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) == 2:
                column1.append(parts[0])
                column2.append(parts[1])
    return [column1, column2]

data = read_data('input1.txt')
print(data)

column1 = list(map(int, data[0]))
column2 = list(map(int, data[1]))

column1.sort()
column2.sort()

total_distance = sum(abs(a - b) for a, b in zip(column1, column2))
print(total_distance)