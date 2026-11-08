"""Board representation: state, FEN parsing, make/unmake move (Phase 2)."""

from engine.constants import EMPTY, OFFBOARD, WHITE, square_from


class Board:
    def __init__(self) -> None:
        self.squares = [OFFBOARD] * 120
        for rank in range(8):
            for file in range(8):
                self.squares[square_from(file, rank)] = EMPTY

        self.side = WHITE
        self.castling = 0
        self.ep_square = 0
        self.halfmove_clock = 0
        self.fullmove_number = 1
        self.king_sq = [0, 0]
        self.history = []
