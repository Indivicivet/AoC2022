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
    inspected: int = 0

    def next_worry(self, worry):
        self.inspected += 1
        if self.mult_by == "SQUARE":
            return worry ** 2
        return worry * self.mult_by

    def throw_to(self, val):
        return (
            self.false_target
            if val % self.divisible_test
            else self.true_target
        )

    def pop_item(self):
        return self.items.pop(0)

    def receive(self, val):
        self.items.append(val)


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
    monkeys.append(
        (
            PlusPlusMonkey
            if "+" in monkey_str
            else MultMultMonkey
        )(
            items,
            op_value,
            div_test,
            true_target,
            false_target,
        )
    )

for monkey in monkeys:
    print(monkey.items)


for round_i in range(20):
    for monkey in monkeys:
        while monkey.items:
            worry_level = monkey.pop_item()
            worry2 = monkey.next_worry(worry_level) // 3
            monkeys[monkey.throw_to(worry2)].receive(worry2)
