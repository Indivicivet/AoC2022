import os
from pathlib import Path

data = (
    Path(__file__).parent / "inputs" / "input_day07.txt"
).read_text().splitlines()

# create structure on filesystem
ROOT = Path(__file__).parent / "day07_working"
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


def get_folder_size(folder):
    return sum(
        subitem.stat().st_size
        for subitem in folder.rglob("*")
        if subitem.is_file()
    )


under_100000_size = 0
for item in ROOT.rglob("*"):
    size = get_folder_size(item)
    if size < 100000:
        under_100000_size += size
print(under_100000_size)


root_size = get_folder_size(ROOT)
smallest_deletable_size = min(
    size
    for item in ROOT.rglob("*")
    if (size := get_folder_size(item)) >= root_size - 40000000
)
print(smallest_deletable_size)
