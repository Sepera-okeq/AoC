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

files = {}
for idx, val in enumerate(positions):
    if val != '.':
        file_id = val
        if file_id not in files:
            files[file_id] = {'start': idx, 'length': 0}
        files[file_id]['length'] += 1
        files[file_id]['end'] = idx

for file_id in sorted(files.keys(), reverse=True):
    file = files[file_id]
    file_start = file['start']
    file_length = file['length']
    free_space_runs = []
    i = 0
    while i < file_start:
        if positions[i] == '.':
            start = i
            while i < file_start and positions[i] == '.':
                i += 1
            end = i - 1
            length = end - start + 1
            if length >= file_length:
                free_space_runs.append({'start': start, 'length': length})
        else:
            i += 1
    if free_space_runs:
        new_location = min(free_space_runs, key=lambda x: x['start'])
        new_start = new_location['start']
        for offset in range(file_length):
            positions[new_start + offset] = file_id
            positions[file_start + offset] = '.'
        files[file_id]['start'] = new_start
        files[file_id]['end'] = new_start + file_length - 1

checksum = 0
for idx, val in enumerate(positions):
    if val != '.':
        checksum += idx * val

print(checksum)