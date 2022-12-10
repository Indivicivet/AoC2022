from pathlib import Path

import openpyscad as ops

data = [
    [int(x) for x in line.strip()]
    for line in (
        Path(__file__).parent.parent / "inputs" / "input_day08.txt"
    ).read_text().splitlines()
]

openscad_obj = ops.Union()
for j in range(len(data)):
    for i in range(len(data[0])):
        openscad_obj.append(
            ops.Cube([0.8, 0.8, data[j][i] + 0.5]).translate([i, j, 0])
        )
openscad_obj.write("day08.scad")
