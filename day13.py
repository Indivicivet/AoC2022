from pathlib import Path


class IntCompList(list):
    def __lt__(self, other):
        return super().__lt__(
            [other]
            if isinstance(other, int)
            else other
        )

    def __gt__(self, other):
        if isinstance(other, int):
            return self > [other]
        return super().__gt__(other)

    def __eq__(self, other):
        if isinstance(other, int):
            return self == [other]
        return super().__eq__(other)


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
