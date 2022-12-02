from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional, Callable
from pathlib import Path


@dataclass
class Brainfuck:
    """
    `comma_callback` needs to be set to feed in data via comma operator
    `period_callback` is optional; . will store in `outputs` regardless
    """

    comma_callback: Optional[Callable[[], int]] = None
    period_callback: Optional[Callable[[int], None]] = None
    ignore_other_characters: bool = True
    tape: defaultdict = field(default_factory=lambda: defaultdict(int))
    outputs: list = field(default_factory=list)
    ptr: int = 0

    def execute(self, code):
        if self.comma_callback is None and "," in code:
            raise ValueError(
                "got code containing \",\", but comma_callback"
                "is not set for this brainfuck interpreter"
            )
        code_ptr = 0
        brackets_depth = 0
        while code_ptr < len(code):
            char = code[code_ptr]
            if char == "+":
                self.tape[self.ptr] += 1
            elif char == "-":
                self.tape[self.ptr] -= 1
            elif char == ">":
                self.ptr += 1
            elif char == "<":
                self.ptr -= 1
            elif char == ".":
                self.outputs.append(self.tape[self.ptr])
                if self.period_callback is not None:
                    self.period_callback(self.tape[self.ptr])
            elif char == ",":
                self.tape[self.ptr] = self.comma_callback()
            elif char == "[":
                brackets_depth += 1
                if not self.tape[self.ptr]:
                    # skip forward
                    start_depth = brackets_depth
                    while brackets_depth >= start_depth and code_ptr < len(code):
                        code_ptr += 1
                        char = code[code_ptr]
                        if char == "[":
                            brackets_depth += 1
                        elif char == "]":
                            brackets_depth -= 1
            elif char == "]":
                brackets_depth -= 1
                if self.tape[self.ptr]:
                    # skip backward
                    start_depth = brackets_depth
                    while brackets_depth <= start_depth and code_ptr >= 0:
                        code_ptr -= 1
                        char = code[code_ptr]
                        if char == "[":
                            brackets_depth += 1
                        elif char == "]":
                            brackets_depth -= 1
            elif char in " \t\n" or self.ignore_other_characters:
                pass
            else:
                raise ValueError(f"encountered invalid character {char!r}")
            code_ptr += 1

    def execute_file(self, path):
        """
        helper function to execute code in a .b file
        """
        self.execute(Path(path).read_text())


if __name__ == "__main__":
    bf = Brainfuck(comma_callback=lambda: 4)
    bf.execute("+. >--. >+++[->+<]>. >,.")  #
    print(bf.tape)
    print(bf.outputs)
