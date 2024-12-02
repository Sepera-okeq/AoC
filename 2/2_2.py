with open('input (1).txt', 'r', encoding='utf-8') as file:
    data = file.read()

def is_safe_fake(report):
    def is_safe(report):
        inc = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
        dec = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
        return inc or dec

    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports(data):
    reports = [list(map(int, line.split())) for line in data.strip().split('\n')]
    return sum(1 for report in reports if is_safe_fake(report))

print(count_safe_reports(data))