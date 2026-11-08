"""Constants and square helpers shared by the whole engine."""

# Starting position
STARTING_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

# Colors
WHITE = 0
BLACK = 1

# Pieces
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6
OFFBOARD = 7

# Castling squares (back ranks, as 10x12 mailbox indices)
A1 = 21
B1 = 22
C1 = 23
D1 = 24
E1 = 25
F1 = 26
G1 = 27
H1 = 28

A8 = 91
B8 = 92
C8 = 93
D8 = 94
E8 = 95
F8 = 96
G8 = 97
H8 = 98

# Directions
NORTH = 10
SOUTH = -10
EAST = 1
WEST = -1

# Piece directions (offsets added to a square index)
ROOK_DIRS = (NORTH, SOUTH, EAST, WEST)

BISHOP_DIRS = (
    NORTH + EAST,   # up-right
    NORTH + WEST,   # up-left
    SOUTH + EAST,   # down-right
    SOUTH + WEST,   # down-left
)

KING_DIRS = ROOK_DIRS + BISHOP_DIRS   # all 8 directions, one step at a time

KNIGHT_DIRS = (
    NORTH + NORTH + EAST,   # up 2, right 1
    NORTH + NORTH + WEST,   # up 2, left 1
    SOUTH + SOUTH + EAST,   # down 2, right 1
    SOUTH + SOUTH + WEST,   # down 2, left 1
    EAST + EAST + NORTH,    # right 2, up 1
    EAST + EAST + SOUTH,    # right 2, down 1
    WEST + WEST + NORTH,    # left 2, up 1
    WEST + WEST + SOUTH,    # left 2, down 1
)

# Castling bits
WK = 1   # 0001  white kingside
WQ = 2   # 0010  white queenside
BK = 4   # 0100  black kingside
BQ = 8   # 1000  black queenside

CASTLE_CHAR_TO_BIT = {"K": WK, "Q": WQ, "k": BK, "q": BQ}

# Piece <-> FEN character
CHAR_TO_PIECE = {
    # White pieces: uppercase, positive
    "P": PAWN,
    "N": KNIGHT,
    "B": BISHOP,
    "R": ROOK,
    "Q": QUEEN,
    "K": KING,
    # Black pieces: lowercase, negative
    "p": -PAWN,
    "n": -KNIGHT,
    "b": -BISHOP,
    "r": -ROOK,
    "q": -QUEEN,
    "k": -KING,
}

PIECE_TO_CHAR = {value: key for key, value in CHAR_TO_PIECE.items()}


# Helpers
def square_from(file: int, rank: int) -> int:
    """Convert a file and rank (both 0-7) to a 120-index (e.g. 4, 3 -> 55)."""
    return 21 + file + 10 * rank


def file_of(sq: int) -> int:
    """Return the file (0-7, a-h) of a 120-index (e.g. 55 -> 4)."""
    return sq % 10 - 1


def rank_of(sq: int) -> int:
    """Return the rank (0-7, ranks 1-8) of a 120-index (e.g. 55 -> 3)."""
    return sq // 10 - 2


def str_to_square(name: str) -> int:
    """Convert algebraic notation (e.g. 'e4') to a 120-index (e.g. 55)."""
    file = ord(name[0].lower()) - ord("a")
    rank = int(name[1]) - 1
    return square_from(file, rank)


def square_to_str(sq: int) -> str:
    """Convert a 120-index (e.g. 21) to algebraic notation (e.g. 'a1')."""
    file = file_of(sq)
    rank = rank_of(sq)
    return chr(ord("a") + file) + str(rank + 1)
