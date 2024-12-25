from typing import Callable, List, Dict

def perform_operation(left: int, right: int, operation: str) -> int:
    if operation == "AND":
        return left & right
    elif operation == "OR":
        return left | right
    elif operation == "XOR":
        return left ^ right

def find_value(value: str, wires: Dict[str, int], gates: List[Dict[str, str]]) -> int:
    if value.isdigit():
        return int(value)

    for g in gates:
        if g["output_wire"] == value:
            left, right = wires.get(g["left"]), wires.get(g["right"])
            if left is None:
                left_value = find_value(g["left"], wires, gates)
                wires[g["left"]] = left_value
                return find_value(value, wires, gates)

            if right is None:
                right_value = find_value(g["right"], wires, gates)
                wires[g["right"]] = right_value
                return find_value(value, wires, gates)

            return perform_operation(left, right, g["operation"])

    return -1

wires, g = open("input (23).txt").read().split("\n\n")
wires = {w.split(":")[0]: int(w.split(":")[1]) for w in wires.strip().split("\n")}
gates = []
for gate in [wire for wire in g.strip().split("\n")]:
    left, operation, right, _, output_wire = gate.split(" ")
    gates.append({"left": left, "right": right, "output_wire": output_wire, "operation": operation.upper()})

def get_number(filt: Callable[[str], bool], wires: Dict[str, int], gates: List[Dict[str, str]]) -> int:
    for gate in gates:
        left, right = wires.get(gate["left"]), wires.get(gate["right"])
        if left is None or right is None:
            result = find_value(gate["output_wire"], wires, gates)
            if result == -1:
                assert False, f"Should never happen: {result}"
        else:
            result = perform_operation(left, right, gate["operation"])

        wires[gate["output_wire"]] = result

    num = 0
    for key in sorted(filter(filt, wires.keys()), reverse=True):
        num = (num << 1) | wires[key]

    return num

print(get_number(lambda x: x.startswith("z"), wires, gates))
