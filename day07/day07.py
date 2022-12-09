import os
from pathlib import Path

data = (
    Path(__file__).parent.parent / "inputs" / "input_day07.txt"
).read_text().splitlines()

# create structure on filesystem
ROOT = Path(__file__).parent / "working"
ROOT.mkdir(exist_ok=True, parents=True)
os.chdir(ROOT)
for line in data[1:]:
    if line == "$ ls":
        # we can tell just by it being a file/dir
        continue
    elif line[:4] == "$ cd":
        os.chdir(line.split(" ")[2])
    else:
        value, name = line.split(" ")
        if value == "dir":
            (Path.cwd() / name).mkdir(exist_ok=True)
        else:
            (Path.cwd() / name).write_bytes(b"!" * int(value))


under_100000_size = 0
for item in ROOT.rglob("*"):
    size = sum(
        subitem.stat().st_size
        for subitem in item.rglob("*")
    )
    if size < 100000:
        under_100000_size += size
print(under_100000_size)