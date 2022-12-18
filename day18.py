from pathlib import Path

import openpyscad as ops

data = [
    [int(x) for x in line.split(",")]
    for line in (
        Path(__file__).parent / "inputs" / "input_day18.txt"
    ).read_text().splitlines()
]

print(data)
