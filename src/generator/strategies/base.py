from typing import Protocol
import random

from ...board import Board


class GenerationStrategy(Protocol):
    def generate(self, board: Board, rng: random.Random) -> None:
        pass