# src/sudoku/generator.py
import random
from enum import StrEnum

from ..board import Board
from .strategies.backtracking import BacktrackingStrategy
from .strategies.permutations import PermutationStrategy
from .strategies.seeding_and_propagation import SeedingAndPropagationStrategy


class GenerationAlgorithm(StrEnum):
    BACKTRACKING = "backtracking"
    PERMUTATIONS = "permutations"
    SEEDING_AND_PROPAGATION = "seeding_and_propagation"


class Generator:
    def __init__(
        self,
        size: int = 9,
        seed: int | None = None,
    ) -> None:
        self.board = Board(size)
        self.rng = random.Random(seed)

        self._strategies = {
            GenerationAlgorithm.BACKTRACKING: BacktrackingStrategy(),
            GenerationAlgorithm.PERMUTATIONS: PermutationStrategy(),
            GenerationAlgorithm.SEEDING_AND_PROPAGATION: SeedingAndPropagationStrategy(),
        }

    def generate(
        self,
        algorithm: GenerationAlgorithm = GenerationAlgorithm.PERMUTATIONS,
    ) -> Board:
        try:
            strategy = self._strategies[algorithm]
        except KeyError as error:
            raise ValueError(f"Unsupported algorithm: {algorithm}") from error

        strategy.generate(self.board, self.rng)

        if not self.board.is_valid():
            raise RuntimeError(f"{algorithm} produced an invalid board")

        return self.board