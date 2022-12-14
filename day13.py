from pathlib import Path


def force_list(x):
    if isinstance(x, int):
        return [x]
    return x


class IntCompList(list):
    __lt__ = lambda self, x: super().__lt__(force_list(x))
    __gt__ = lambda self, x: super().__gt__(force_list(x))
    __eq__ = lambda self, x: super().__eq__(force_list(x))


packet_pairs = [
    pair.splitlines()
    for pair in (
        Path(__file__).parent / "inputs" / "input_day13.txt"
    ).read_text().replace("[", "IntCompList([").replace("]", "])").split("\n\n")
]

print(sum(
    i + 1
    for i, (a, b) in enumerate(packet_pairs)
    if eval(a) < eval(b)
))
