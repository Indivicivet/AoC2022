from pathlib import Path

from python_utils import brainfuck

FOLDER = Path(__file__).parent


def read_file():
    for line in (
        FOLDER / "inputs" / "input_day01.txt"
    ).read_text().splitlines():
        yield int(line) if line else 0
    yield 0  # just to make my life easier ^^'
    while True:
        yield -1


bf = brainfuck.Brainfuck(
    comma_callback=read_file().__next__,
    # period_callback=print,
)

bf.execute((FOLDER / "day01_part1_sum_chunks.b").read_text())

# part 1
print(max(bf.outputs))

bf_pt2 = brainfuck.Brainfuck(
    comma_callback=iter(sorted(bf.outputs, reverse=True)).__next__,
    period_callback=print,
)

bf_pt2.execute((FOLDER / "day01_part2_sum3.b").read_text())
