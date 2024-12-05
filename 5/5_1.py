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

rules, updates = read_input("input (4).txt")

rule_dict = {}
for X, Y in rules:
    if X not in rule_dict:
        rule_dict[X] = []
    rule_dict[X].append(Y)

valid_middle_pages = []
for update in updates:
    if validate_update(update, rule_dict):
        middle_page = update[len(update) // 2]
        valid_middle_pages.append(middle_page)

print(sum(valid_middle_pages))