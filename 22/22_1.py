with open('input (21).txt', 'r') as file:
    secret_numbers = list(map(int, file.readlines()))

result = 0

for secret_number in secret_numbers:
    for _ in range(2000):
        secret_number = (secret_number ^ (secret_number * 64)) % 16777216
        secret_number = (secret_number ^ (secret_number // 32)) % 16777216
        secret_number = (secret_number ^ (secret_number * 2048)) % 16777216
    result += secret_number

print(result)