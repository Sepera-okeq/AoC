from collections import deque

with open("input (10).txt", "r") as file:
    stones = list(map(int, file.readline().strip().split()))

iterations = 75

current_counts = {stone: 1 for stone in stones}

for _ in range(iterations):
    next_counts = {}
    for stone, count in current_counts.items():
        if stone == 0:
            next_counts[1] = next_counts.get(1, 0) + count
        elif len(str(stone)) % 2 == 0:
            n = len(str(stone))
            left_half = int(str(stone)[:n // 2])
            right_half = int(str(stone)[n // 2:])
            next_counts[left_half] = next_counts.get(left_half, 0) + count
            next_counts[right_half] = next_counts.get(right_half, 0) + count
        else:
            new_stone = stone * 2024
            next_counts[new_stone] = next_counts.get(new_stone, 0) + count
    current_counts = next_counts

print(sum(current_counts.values()))