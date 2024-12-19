from functools import lru_cache

with open('input (18).txt', 'r') as file:
    content = file.read()

patterns_section, designs_section = content.strip().split('\n\n')
towel_patterns = patterns_section.split(', ')
desired_designs = designs_section.split('\n')

@lru_cache(None)
def count_ways_to_make_design(design):
    if not design:
        return 1

    total_ways = 0

    for pattern in towel_patterns:
        if design.startswith(pattern):
            total_ways += count_ways_to_make_design(design[len(pattern):])

    return total_ways

count = 0

for design in desired_designs:
    count += count_ways_to_make_design(design)

print(count)