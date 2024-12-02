with open('input (1).txt', 'r', encoding='utf-8') as file:
    data = file.read()

def is_safe(report):
    inc = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    dec = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return inc or dec

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data.strip().split('\n')]
    return sum(1 for report in reports if is_safe(report))

print(count_safe_reports(data))