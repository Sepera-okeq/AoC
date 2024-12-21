import sys
import itertools

with open('input (20).txt', 'r') as file:
    lines = file.read().strip().splitlines()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class Direction:
    N = 'N'
    E = 'E'
    S = 'S'
    W = 'W'

    directions = [N, E, S, W]
    moves = {
        N: (0, -1),
        E: (1, 0),
        S: (0, 1),
        W: (-1, 0),
    }

    symbols = {
        N: ord('^'),
        E: ord('>'),
        S: ord('v'),
        W: ord('<'),
    }

door_keys = [
    (Point(0, 0), ord('7')),
    (Point(1, 0), ord('8')),
    (Point(2, 0), ord('9')),
    (Point(0, 1), ord('4')),
    (Point(1, 1), ord('5')),
    (Point(2, 1), ord('6')),
    (Point(0, 2), ord('1')),
    (Point(1, 2), ord('2')),
    (Point(2, 2), ord('3')),
    (Point(1, 3), ord('0')),
    (Point(2, 3), ord('A')),
]

robot_keys = [
    (Point(1, 0), ord('^')),
    (Point(2, 0), ord('A')),
    (Point(0, 1), ord('<')),
    (Point(1, 1), ord('v')),
    (Point(2, 1), ord('>')),
]

def create_keypad(keys):
    keypad_map = {}
    positions = {}
    for point, value in keys:
        keypad_map[(point.x, point.y)] = value
        positions[value] = point
    return keypad_map, positions

door_map, door_positions = create_keypad(door_keys)
robot_map, robot_positions = create_keypad(robot_keys)

targets = []
for line in lines:
    if line.endswith('A'):
        number = int(line[:-1])
        seq = [ord(c) for c in line]
        targets.append((number, seq))
    else:
        sys.exit('fuck to strip letter')

depth = 2

cache = {}

def traverse(keypad_map, keypad_positions, a, b, depth):
    key = (a, b, depth)
    if key in cache:
        return cache[key]

    from_point = keypad_positions[a]
    to_point = keypad_positions[b]

    if depth == 0:
        result = from_point.distance(to_point) + 1
        cache[key] = result
        return result

    moves = []
    if from_point.x < to_point.x:
        moves.extend([Direction.E] * (to_point.x - from_point.x))
    else:
        moves.extend([Direction.W] * (from_point.x - to_point.x))

    if from_point.y < to_point.y:
        moves.extend([Direction.S] * (to_point.y - from_point.y))
    else:
        moves.extend([Direction.N] * (from_point.y - to_point.y))

    min_result = None
    for perm in set(itertools.permutations(moves)):
        p = from_point
        valid = True
        for d in perm:
            dx, dy = Direction.moves[d]
            next_x = p.x + dx
            next_y = p.y + dy
            if (next_x, next_y) in keypad_map:
                p = Point(next_x, next_y)
            else:
                valid = False
                break
        if valid:
            seq = [ord('A')] + [Direction.symbols[d] for d in perm] + [ord('A')]
            total = 0
            for a_char, b_char in zip(seq[:-1], seq[1:]):
                total += traverse(robot_map, robot_positions, a_char, b_char, depth - 1)
            if min_result is None or total < min_result:
                min_result = total

    if min_result is None:
        sys.exit('fuck to find move set')

    cache[key] = min_result
    return min_result

total_sum = 0
for number, seq in targets:
    total_moves = 0
    seq_chars = [ord('A')] + seq
    for a_char, b_char in zip(seq_chars[:-1], seq_chars[1:]):
        total_moves += traverse(door_map, door_positions, a_char, b_char, depth)
    total_sum += number * total_moves

print(total_sum)