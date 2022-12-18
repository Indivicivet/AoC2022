import re
from dataclasses import dataclass
from pathlib import Path

import cppyy


@dataclass
class MultMultMonkey:
    items: list[int]
    mult_by: int
    divisible_test: int
    true_target: int
    false_target: int


cppyy.cppdef(Path("day11_++monkey.cpp").read_text())
from cppyy.gbl import PlusPlusMonkey


monkey_strs = (
    Path(__file__).parent / "inputs" / "input_day11.txt"
).read_text().split("\n\n")


def find_numbers(s):
    return (
        [int(x) for x in re.findall(r"\d+", s)]
        or ["SQUARE"]  # nonsense special case old * old
    )


monkeys = []
for i, monkey_str in enumerate(monkey_strs):
    lines = monkey_str.splitlines()
    items = find_numbers(lines[1])
    op_value, div_test, true_target, false_target = [
        find_numbers(line)[0]
        for line in lines[2:]
    ]
    if "*" in monkey_str:
        monkeys.append(
            MultMultMonkey(
                items,
                op_value,
                div_test,
                true_target,
                false_target,
            )
        )
    else:
        monkeys.append(
            PlusPlusMonkey(
                items,
                op_value,
                div_test,
                true_target,
                false_target,
            )
        )

print(monkeys)