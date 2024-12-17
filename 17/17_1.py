import os
from functools import reduce

with open("input (16).txt", "r") as file:
    input_file = file.read().splitlines()

a, b, c = int(input_file[0][11:]), int(input_file[1][11:]), int(input_file[2][11:])
program = eval("[" + input_file[-1][9:] + "]")

ip = 0
output = []

while ip < len(program) - 1:
    opcode = program[ip]
    operand = program[ip + 1]
    coperand = 0
    if operand in {0, 1, 2, 3}:
        coperand = operand
    elif operand == 4:
        coperand = a
    elif operand == 5:
        coperand = b
    elif operand == 6:
        coperand = c
    
    if opcode == 0:
        a //= 2 ** coperand
    elif opcode == 1:
        b ^= operand
    elif opcode == 2:
        b = coperand % 8
    elif opcode == 3:
        if a != 0:
            ip = operand - 2
    elif opcode == 4:
        b ^= c
    elif opcode == 5:
        output.append(coperand % 8)
    elif opcode == 6:
        b = a // 2 ** coperand
    elif opcode == 7:
        c = a // 2 ** coperand
    
    ip += 2

result = ",".join(map(str, output))
print(result)