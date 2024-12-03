import re

with open('input (2).txt', 'r', encoding='utf-8') as file:
    data = file.read()

def extract_and_multiply(expression):
    pattern = r'mul\((\d+),(\d+)\)'
    matches = re.findall(pattern, expression)
    
    total = 0
    for match in matches:
        x, y = map(int, match)
        total += x * y
    
    return total

print(extract_and_multiply(data))