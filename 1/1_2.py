from collections import Counter

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

count_column1 = Counter(column1)
count_column2 = Counter(column2)
similarity_score = 0
for num in column1:
    if num in count_column2:
        similarity_score += num * count_column2[num]

print("similarity score:", similarity_score)
