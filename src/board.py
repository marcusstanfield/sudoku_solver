from dataclasses import dataclass
import math
import numpy as np


@dataclass
class Board:
    size: int = 9

    def __post_init__(self) -> None:
        self.box_size = math.isqrt(self.size)

        if self.box_size**2 != self.size:
            raise ValueError("Board size must be a perfect square.")

        self.grid = np.zeros((self.size, self.size), dtype=int)

    @property
    def numbers(self) -> set[int]:
        return set(range(1, self.size + 1))

    def is_valid(self) -> bool:
        expected = self.numbers

        for row in self.grid:
            if set(row) != expected:
                return False

        for column in self.grid.T:
            if set(column) != expected:
                return False

        for row_start in range(0, self.size, self.box_size):
            for column_start in range(0, self.size, self.box_size):
                box = self.grid[
                    row_start:row_start + self.box_size,
                    column_start:column_start + self.box_size,
                ]
                if set(box.flat) != expected:
                    return False

        return True