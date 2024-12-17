import os
from functools import reduce

with open("input (16).txt", "r") as file:
    input_file = file.read().splitlines()

program = eval("[" + input_file[-1][9:] + "]")

guess = [0]
while True:
    value = reduce(lambda a, b: (a << 3) + b, guess)
    
    a, b, c = value, 0, 0
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

    if output[-len(guess):] != program[-len(guess):]:
        while guess[-1] == 7:
            guess.pop()
        
        guess[-1] += 1
    elif output == program:
        print(value)
        break
    else:
        guess.append(0)