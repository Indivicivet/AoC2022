from pathlib import Path

from python_utils import brainfuck

FOLDER = Path(__file__).parent

data = [
    [
        int(val)
        for range_ in line.split(",")
        for val in range_.split("-")
    ]
    for line in (
        FOLDER / "inputs" / "input_day04.txt"
    ).read_text().splitlines()
]

bf = brainfuck.Brainfuck(
    comma_callback=iter(data[0]).__next__,
)
bf.execute_file("day04_part1_is_containment.b")
print([bf.tape.get(i) for i in range(15)])
print(bf.outputs)
