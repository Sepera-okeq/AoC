from collections import deque

with open("input (10).txt", "r") as file:
    stones = deque(map(int, file.readline().strip().split()))

iterations = 25

for _ in range(iterations):
    new_stones = deque()
    for _ in range(len(stones)):
        stone = stones.popleft()
        if stone == 0:
            new_stones.append(1)
        else:
            stone_str = str(stone)
            length = len(stone_str)
            if length % 2 == 0:
                left_half = stone_str[:length//2]
                right_half = stone_str[length//2:]
                new_stones.append(int(left_half) if left_half != '' else 0)
                new_stones.append(int(right_half) if right_half != '' else 0)
            else:
                new_stone = stone * 2024
                new_stones.append(new_stone)
    stones.extend(new_stones)

print(len(stones))