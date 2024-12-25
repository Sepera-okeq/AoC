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

def find_output_wire(left: str, right: str, operation: str, gates: List[Dict[str, str]]) -> str:
    for g in gates:
        if g["left"] == left and g["right"] == right and g["operation"] == operation:
            return g["output_wire"]
        if g["left"] == right and g["right"] == left and g["operation"] == operation:
            return g["output_wire"]
    return None

def full_adder_logic(x: str, y: str, c0: str, gates: List[Dict[str, str]], swapped: List[str]) -> (str, str):
    m1 = find_output_wire(x, y, "XOR", gates)
    n1 = find_output_wire(x, y, "AND", gates)

    assert m1 is not None, f"m1 is None for {x}, {y}"
    assert n1 is not None, f"n1 is None for {x}, {y}"

    if c0 is not None:
        r1 = find_output_wire(c0, m1, "AND", gates)
        if not r1:
            n1, m1 = m1, n1
            swapped.append(m1)
            swapped.append(n1)
            r1 = find_output_wire(c0, m1, "AND", gates)

        z1 = find_output_wire(c0, m1, "XOR", gates)

        if m1 and m1.startswith("z"):
            m1, z1 = z1, m1
            swapped.append(m1)
            swapped.append(z1)

        if n1 and n1.startswith("z"):
            n1, z1 = z1, n1
            swapped.append(n1)
            swapped.append(z1)

        if r1 and r1.startswith("z"):
            r1, z1 = z1, r1
            swapped.append(r1)
            swapped.append(z1)

        assert r1 is not None, f"r1 is None for {c0}, {m1}"
        assert n1 is not None, f"n1 is None for {c0}, {m1}"

        c1 = find_output_wire(r1, n1, "OR", gates)
    else:
        z1 = m1
        c1 = n1

    return z1, c1


wires, gates = open("input (23).txt").read().split("\n\n")
wires = {w.split(":")[0]: int(w.split(":")[1]) for w in wires.strip().split("\n")}
gates = []
for gate in [wire for wire in g.strip().split("\n")]:
    left, operation, right, _, output_wire = gate.split(" ")
    gates.append({"left": left, "right": right, "output_wire": output_wire, "operation": operation.upper()})

get_number(lambda x: x.startswith("z"), wires, gates)

c0 = None
swapped = []

bits = len([wire for wire in wires if wire.startswith("x")])
for i in range(bits):
    n = str(i).zfill(2)
    x = f"x{n}"
    y = f"y{n}"

    z1, c1 = full_adder_logic(x, y, c0, gates, swapped)

    if c1 and c1.startswith("z") and c1 != "z45":
        c1, z1 = z1, c1
        swapped.append(c1)
        swapped.append(z1)

    c0 = c1 if c1 else find_output_wire(x, y, "AND", gates)

print(",".join(sorted(swapped)))