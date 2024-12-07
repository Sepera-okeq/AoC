def eval_express(num, operators):
    result = num[0]
    i = 0
    while i < len(operators):
        if operators[i] == '+':
            result += num[i + 1]
        elif operators[i] == '*':
            result *= num[i + 1]
        elif operators[i] == '|':
            result = int(str(result) + str(num[i + 1]))
        i += 1
    return result

def gen_operators(length):
    if length == 0:
        return ['']
    sm = gen_operators(length - 1)
    return [s + op for s in sm for op in '+*|']

def is_valid_equation(target, num):
    for ops in gen_operators(len(num) - 1):
        if eval_express(num, ops) == target:
            return True
    return False

total_result = 0
with open('input (6).txt', 'r') as file:
    for line in file:
        target, num = line.split(':')
        target = int(target)
        num = list(map(int, num.split()))
        if is_valid_equation(target, num):
            total_result += target
print(total_result)