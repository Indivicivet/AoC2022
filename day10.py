from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np
from PIL import Image


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
        head, *tail = self.pending
        head.remaining_cycles -= 1
        if not head.remaining_cycles:
            self.x = head.action(self.x)
            self.pending = tail


data = (
    Path(__file__).parent / "inputs" / "input_day10.txt"
).read_text()

SELECT_SIGNAL_STRENGTHS = [20, 60, 100, 140, 180, 220]

cpu = CPU(
    pending=[
        Instruction.from_str(line)
        for line in data.splitlines()
    ],
)

signal_strength_total = 0
image = np.zeros((6, 40))
for i in range(240):
    image.flat[i] = abs(cpu.x - (i % 40)) <= 1
    if i + 1 in SELECT_SIGNAL_STRENGTHS:
        signal_strength_total += (i + 1) * cpu.x
    cpu.cycle()
print(signal_strength_total)
Image.fromarray(image * 255).show()
