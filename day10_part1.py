from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable


@dataclass
class Instruction:
    action: Callable[[int], int]
    remaining_cycles: int

    @classmethod
    def from_str(cls, s):
        instr_type, *args = s.split()
        if instr_type == "noop":
            return cls(lambda x: x, 1)
        if instr_type == "addx":
            return cls(lambda x: x + int(args[0]), 2)
        raise ValueError(f"unknown instruction {instr_type} in {s}")


@dataclass
class CPU:
    x: int = 1  # the only register
    pending: list[Instruction] = field(default_factory=list)

    def cycle(self):
        self.pending[0].remaining_cycles -= 1
        if not self.pending[0].remaining_cycles:
            self.x = self.pending[0].action(self.x)
            self.pending.pop(0)


data = (
    Path(__file__).parent / "inputs" / "input_day10.txt"
).read_text()
print(len(data.splitlines()))
SELECT_SIGNAL_STRENGTHS = [20, 60, 100, 140, 180, 220]

cpu = CPU(
    pending=[
        Instruction.from_str(line)
        for line in data.splitlines()
    ],
)

signal_strength_total = 0
for i in range(1, max(SELECT_SIGNAL_STRENGTHS) + 1):
    cpu.cycle()
    if i + 1 in SELECT_SIGNAL_STRENGTHS:
        print(i + 1, cpu.x)
        signal_strength_total += (i + 1) * cpu.x
print(signal_strength_total)
