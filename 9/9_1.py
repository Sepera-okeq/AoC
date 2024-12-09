with open('input (8).txt', 'r', encoding='utf-8') as file:
    disk_map = file.read()

positions = []
file_id = 0
i = 0
while i < len(disk_map):
    file_length = int(disk_map[i])
    i += 1
    free_space_length = int(disk_map[i]) if i < len(disk_map) else 0
    i += 1
    positions.extend([file_id]*file_length)
    positions.extend(['.']*free_space_length)
    file_id += 1

while True:
    try:
        left_index = positions.index('.')
    except ValueError:
        break
    try:
        right_index = len(positions) - 1 - positions[::-1].index(next(x for x in reversed(positions) if x != '.'))
    except StopIteration:
        break
    if left_index >= right_index:
        break
    positions[left_index] = positions[right_index]
    positions[right_index] = '.'

checksum = 0
for idx, val in enumerate(positions):
    if val != '.':
        checksum += idx * val

print(checksum)