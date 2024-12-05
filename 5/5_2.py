def read_input(filename):
    with open(filename, "r") as file:
        data = file.read()
    rules_section, updates_section = data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates

def validate_update(update, rule_dict):
    positions = {page: index for index, page in enumerate(update)}
    for X in rule_dict:
        if X in positions:
            for Y in rule_dict[X]:
                if Y in positions and positions[X] > positions[Y]:
                    return False
    return True

from collections import defaultdict, deque

def fuck_sort(pages, rule_dict):
    in_degree = defaultdict(int)
    graph = defaultdict(list)
    for X in pages:
        for Y in rule_dict.get(X, []):
            if Y in pages:
                graph[X].append(Y)
                in_degree[Y] += 1
                in_degree.setdefault(X, 0)
    
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []
    
    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_pages

rules, updates = read_input("input (4).txt")

rule_dict = defaultdict(list)
for X, Y in rules:
    rule_dict[X].append(Y)

incorrect_updates = []
for update in updates:
    if not validate_update(update, rule_dict):
        incorrect_updates.append(update)

corrected_middle_pages = []
for update in incorrect_updates:
    sorted_update = fuck_sort(update, rule_dict)
    middle_page = sorted_update[len(sorted_update) // 2]
    corrected_middle_pages.append(middle_page)

print(sum(corrected_middle_pages))