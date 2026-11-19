"""Board representation: state, FEN parsing, make/unmake move."""

from engine.constants import (
    EMPTY, OFFBOARD, WHITE, BLACK,
    CASTLE_CHAR_TO_BIT, CHAR_TO_PIECE,
    square_from, str_to_square,
)


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

        rank, file = 7, 0
        for c in fields[0]:
            if c == "/":
                rank -= 1
                file = 0
            elif c.isdigit():
                file += int(c)
            else:
                piece = CHAR_TO_PIECE[c]
                square = square_from(file, rank)
                self.squares[square] = piece
                if c == "K":
                    self.king_sq[WHITE] = square
                elif c == "k":
                    self.king_sq[BLACK] = square
                file += 1

        self.side = WHITE if fields[1] == "w" else BLACK

        self.castling = 0
        for c in fields[2]:
            self.castling |= CASTLE_CHAR_TO_BIT.get(c, 0)

        self.ep_square = 0 if fields[3] == "-" else str_to_square(fields[3])

        self.halfmove_clock = int(fields[4])
        self.fullmove_number = int(fields[5])
        