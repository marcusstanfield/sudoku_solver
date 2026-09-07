from .board import Board


def format_board(board: Board) -> str:
    lines = []
    for row_index, row in enumerate(board.grid):
        if row_index and row_index % board.box_size == 0:
            lines.append("-" * (board.size * 2 + board.box_size - 1))

        values = []
        for column_index, value in enumerate(row):
            if column_index and column_index % board.box_size == 0:
                values.append("|")

            values.append(str(value))
        lines.append(" ".join(values))

    return "\n".join(lines)