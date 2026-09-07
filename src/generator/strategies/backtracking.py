import random

from ...board import Board


class BacktrackingStrategy:
    def generate(self, board: Board, rng: random.Random) -> None:
        self._fill(board, rng)

    def _fill(self, board: Board, rng: random.Random) -> bool:
        empty_cell = self._find_empty_cell(board)

        if empty_cell is None:
            return True

        row, column = empty_cell
        candidates = list(self._candidates(board, row, column))
        rng.shuffle(candidates)

        for value in candidates:
            board.grid[row, column] = value

            if self._fill(board, rng):
                return True

            board.grid[row, column] = 0

        return False

    def _find_empty_cell(self, board: Board) -> tuple[int, int] | None:
        for row in range(board.size):
            for column in range(board.size):
                if board.grid[row, column] == 0:
                    return row, column
        return None

    def _candidates(self, board: Board, row: int, column: int) -> set[int]:
        used = set(board.grid[row, :])
        used.update(board.grid[:, column])

        box_size = board.box_size
        row_start = row // box_size * box_size
        column_start = column // box_size * box_size
        box = board.grid[
            row_start:row_start + box_size,
            column_start:column_start + box_size,
        ]
        used.update(box.flat)

        return board.numbers - used