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
        for instruction in self.pending[:]:
            instruction.remaining_cycles -= 1
            if not instruction.remaining_cycles:
                self.x = instruction.action(self.x)
                print(instruction.action(0))
                self.pending.remove(instruction)


data = (
    Path(__file__).parent / "inputs" / "input_day10.txt"
).read_text()
print(len(data.splitlines()))
SELECT_SIGNAL_STRENGTHS = [20, 60, 100, 140, 180, 220]

cpu = CPU()
signal_strength_total = 0
for i, line in enumerate(data.splitlines() + ["noop"] * 3):
    cpu.pending.append(Instruction.from_str(line))
    if i + 1 in SELECT_SIGNAL_STRENGTHS:
        print(i + 1, cpu.x)
        signal_strength_total += (i + 1) * cpu.x
    cpu.cycle()
print(signal_strength_total)
