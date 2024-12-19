with open('input (18).txt', 'r') as file:
    content = file.read()

patterns_section, designs_section = content.strip().split('\n\n')
towel_patterns = patterns_section.split(', ')
desired_designs = designs_section.split('\n')

def can_make_design(design, patterns):
    n = len(design)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern):i] == pattern:
                dp[i] = dp[i] or dp[i - len(pattern)]
                if dp[i]:
                    break

    return dp[n]

count = 0
for design in desired_designs:
    if can_make_design(design, towel_patterns):
        count += 1

print(count)