from pathlib import Path


def force_list(x):
    if isinstance(x, int):
        return [x]
    return x


class IntCompList(list):
    __lt__ = lambda self, x: super().__lt__(force_list(x))
    __gt__ = lambda self, x: super().__gt__(force_list(x))
    __eq__ = lambda self, x: super().__eq__(force_list(x))


input_comparable = (
    Path(__file__).parent / "inputs" / "input_day13.txt"
).read_text().replace("[", "IntCompList([").replace("]", "])")

packet_pairs = [
    pair.splitlines()
    for pair in input_comparable.split("\n\n")
]
print(sum(
    i + 1
    for i, (a, b) in enumerate(packet_pairs)
    if eval(a) < eval(b)
))

# not the prettiest, but...
divider1 = IntCompList([IntCompList([2])])
divider2 = IntCompList([IntCompList([6])])
sorted_packets = sorted([
    eval(line)
    for line in input_comparable.splitlines()
    if line
] + [divider1, divider2])
print(
    (sorted_packets.index(divider1) + 1)
    * (sorted_packets.index(divider2) + 1)
)
