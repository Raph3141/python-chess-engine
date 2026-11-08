# Chess Engine

A UCI chess engine written from scratch in Python, built as a learning project using the [Chess Programming Wiki](https://www.chessprogramming.org/) as the main reference.

> **Status:** early development.

## Design

| Component | Approach |
|---|---|
| Board | [10x12 mailbox](https://www.chessprogramming.org/10x12_Board), a 120-square array with an off-board sentinel border |
| Moves | Packed into integers (from / to / promotion / flags) |
| Move generation | Pseudo-legal moves, filtered for legality with make/unmake |
| Search *(planned)* | Negamax with alpha-beta, iterative deepening, quiescence search, transposition table |
| Evaluation *(planned)* | Material + piece-square tables, later a tapered evaluation |
| Interface *(planned)* | [UCI](https://www.chessprogramming.org/UCI), works with GUIs such as Cute Chess or Arena |

## Project structure

```
engine/      engine source code (board, move generation, search, ...)
tests/       pytest test suite (planned)
main.py      entry point
```

## Getting started

Requires Python 3.10+.

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py          # run the engine
python -m pytest        # run the tests (once they exist)
```

## Testing

Move generation is checked with [perft](https://www.chessprogramming.org/Perft_Results): the number of leaf nodes at a given depth is compared against known values for standard test positions.
