"""Board representation: state, FEN parsing, make/unmake move."""

from engine.constants import *


class Board:
    def __init__(self) -> None:
        self.squares = [OFFBOARD] * 120
        self._clear()
        self.side = WHITE
        self.castling = 0
        self.ep_square = 0
        self.halfmove_clock = 0
        self.fullmove_number = 1

    def _clear(self) -> None:
        """Empty the playing squares and reset king squares and history."""
        for rank in range(8):
            for file in range(8):
                self.squares[square_from(file, rank)] = EMPTY
        self.king_sq = [0, 0]
        self.history = []

    def set_fen(self, fen: str) -> None:
        """Set up the board from a FEN string."""
        self._clear()

        fields = fen.split()
        self.side = WHITE if fields[1] == "w" else BLACK

        self.castling = 0
        for c in fields[2]:
            self.castling |= CASTLE_CHAR_TO_BIT.get(c, 0)

        self.ep_square = 0 if fields[3] == "-" else str_to_square(fields[3])

        self.halfmove_clock = int(fields[4])
        self.fullmove_number = int(fields[5])
        