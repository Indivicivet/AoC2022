from pathlib import Path

import openpyscad as ops

data = [
    [int(x) for x in line.split(",")]
    for line in (
        Path(__file__).parent / "inputs" / "input_day18.txt"
    ).read_text().splitlines()
]

for pos in data:
    try:
        print(ops.Cube([1.01] * 3).translate(pos))
    except:
        print(f"boop {pos}")

obj = ops.Union([
    ops.Cube([1.01] * 3).translate(pos)
    for pos in data
])
obj.write("day18.scad")
