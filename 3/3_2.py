import re

with open('input (2).txt', 'r', encoding='utf-8') as file:
    data = file.read()

def extract_and_multiply(expression):
    matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', expression)
    
    mul_enabled = True
    total = 0
    for match in matches:
        if match == "do()":
            mul_enabled = True
        elif match == "don't()":
            mul_enabled = False
        else:
            if mul_enabled:
                numbers = re.findall(r'\d+', match)
                num1, num2 = int(numbers[0]), int(numbers[1])
                total += num1 * num2
    
    return total


print(extract_and_multiply(data))