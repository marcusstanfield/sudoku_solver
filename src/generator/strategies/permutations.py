import random

from ...board import Board


class PermutationStrategy:
    def generate(self, board: Board, rng: random.Random) -> None:
        size = board.size
        box_size = board.box_size

        grid = [
            [
                (row * box_size + row // box_size + column) % size + 1
                for column in range(size)
            ]
            for row in range(size)
        ]

        mapping = list(range(1, size + 1))
        rng.shuffle(mapping)
        replacements = dict(zip(range(1, size + 1), mapping))

        board.grid[:] = [
            [replacements[value] for value in row]
            for row in grid
        ]

        # Row, column, band, and stack permutations can live in
        # private helper methods in this class.