from pathlib import Path


def force_list(x):
    if isinstance(x, int):
        return [x]
    return x


class IntCompList(list):
    __lt__ = lambda self, x: super().__lt__(force_list(x))
    __gt__ = lambda self, x: super().__gt__(force_list(x))
    __eq__ = lambda self, x: super().__eq__(force_list(x))


packets = [
    eval(x.replace("[", "IntCompList([").replace("]", "])"))
    for x in (
        Path(__file__).parent / "inputs" / "input_day13.txt"
    ).read_text().splitlines()
    if x
]
print(sum(
    i + 1
    for i, (a, b) in enumerate(zip(packets[::2], packets[1::2]))
    if a < b
))

dividers = [IntCompList([IntCompList([n])]) for n in [2, 6]]
sorted_packets = sorted(packets + dividers)
print(
    (sorted_packets.index(dividers[0]) + 1)
    * (sorted_packets.index(dividers[1]) + 1)
)
