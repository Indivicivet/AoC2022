from pathlib import Path

from python_utils import brainfuck


def read_file():
    for line in (
        Path("inputs") / "input_day01.txt"
    ).read_text().splitlines():
        yield int(line) if line else 0
    yield 0  # just to make my life easier ^^'
    while True:
        yield -1


bf = brainfuck.Brainfuck(
    comma_callback=read_file().__next__,
    period_callback=print,
)

bf.execute("""
while we're still in the file
>+[
    [
        [-<+>]
        ,  should deal with minus 1 better
    ]<-> <.> 
>>,+]
""")  # <<< <<[.<<]

# part 1
print(max(bf.outputs))
