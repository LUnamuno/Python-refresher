# 03 - HilbertMaze

**Codility:** [HilbertMaze](https://app.codility.com/programmers/trainings/2/hilbert_maze/) - Exercise 2, 2016 Contest

Shortest path in a huge recursive (Hilbert-curve) maze, up to 2^26 + 1 cells per side.

## Task description

A halfling is searching for treasure hidden in a maze in the dwarfs' mine. He has a map of the maze and would like to find the shortest path to the treasure.

The maze has a specific shape. It is placed on a square grid with `M^2` cells, where `M = 2^(N+1) + 1` for some given size `N`. Each cell has coordinates `(x, y)`, where `0 <= x, y < M`, and can either be empty or contain a rock. (In the pictures `x` grows to the right and `y` grows upwards; the origin is the bottom-left cell.)

The mazes of sizes `N = 1` and `N = 2` are shown in the original statement as pictures. The maze of size `N = 1` is (`#` = rock, `.` = empty; the top row is `y = 4`):

```
y=4  .....
y=3  .###.
y=2  .#.#.
y=1  .#.#.
y=0  .....
     01234   (x)
```

A maze of size `N` is constructed recursively from the layout of the maze of size `N-1` (like the Hilbert curve). It contains four mazes of size `N-1`, each maze in one quarter. The maze in the bottom-left quarter is rotated by 90 degrees clockwise and the maze in the bottom-right quarter is rotated by 90 degrees counter-clockwise. The mazes in the top quarters are not rotated. There are three additional rocks in the areas where the mazes intersect. (The original statement shows the construction of the maze of size `N = 3` as a picture; the section *Reading the pictures* below gives the exact layout.)

The halfling would like to reach the treasure in the smallest number of steps possible. At each step, he can move to any one of the four adjacent cells (north, south, west, east) that does not contain a rock and is not outside of the grid.

For example, given `N = 1`, the halfling needs 8 steps to move from cell `(2, 1)` to cell `(3, 4)`: down to `(2, 0)`, right to `(4, 0)`, up to `(4, 4)` and left to `(3, 4)`.

Write a function:

```python
def solution(N, A, B, C, D)
```

that, given the size of the maze `N`, coordinates of the halfling `(A, B)` and coordinates of the treasure `(C, D)`, returns the minimum number of steps required for the halfling to reach the treasure.

### Examples

1. Given `N = 1`, `A = 2`, `B = 1`, `C = 3` and `D = 4` the function should return `8`, as shown above.
2. Given `N = 2`, `A = 2`, `B = 5`, `C = 6` and `D = 6` the function should return `7`.
3. Given `N = 3`, `A = 6`, `B = 6`, `C = 10` and `D = 13` the function should return `39`.

### Assumptions

- `N` is an integer within the range `[1..25]`;
- `A`, `B`, `C`, `D` are integers within the range `[0..2^(N+1)]`;
- cells `(A, B)` and `(C, D)` do not contain rocks;
- the result will be an integer smaller than `2,147,483,647`.

Write an **efficient** algorithm.

### Reading the pictures

The pictures cannot be reproduced here, so this is the layout that reproduces all three examples (it is checked by the notebook against a literal construction and BFS):

- the maze of size `0` is a `3 x 3` grid whose only rock is the centre `(1, 1)`;
- the maze of size `N` has `M = 2^(N+1) + 1` and `mid = 2^N`. Its quarters are placed with origins `(0, 0)` (bottom-left, rotated clockwise), `(mid, 0)` (bottom-right, rotated counter-clockwise), `(0, mid)` and `(mid, mid)` (top, not rotated). Neighbouring quarters share one row or column of cells (the middle row `y = mid` and the middle column `x = mid`);
- the three additional rocks are at `(1, mid)`, `(M - 2, mid)` and `(mid, mid + 1)`.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `hilbert_maze.ipynb` | Recursive solution on the maze structure, BFS reference on small mazes, large-N checks. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_2_2016_contest/03_hilbert_maze/requirements.txt
jupyter lab codility/exercise_2_2016_contest/03_hilbert_maze/hilbert_maze.ipynb
```

## Hints

1. The grid can have up to `(2^26 + 1)^2` cells: a BFS is impossible. Use the structure.
2. Rocks sit on a Hilbert curve (the centres of the `4^N` blocks plus the cells joining consecutive blocks). The empty cells are **the walls of a perfect maze** whose corridor is that curve, so the graph of empty cells has exactly **one cycle**: the outer border of the grid. Everything else is a set of trees hanging from single border cells.
3. Two cells hanging from different border cells: walk to the border, go around it the short way, walk into the other tree.
4. Inside the maze of size `N` the "skeleton" is the border plus the middle cross (a T-shaped tree plus a short top column). Every cell of a quarter hangs from a skeleton cell, through the same structure one level down. Recursion depth: `N`.
5. If both cells hang from the same skeleton cell of the same quarter, recurse into that quarter. Verify with a literal construction and BFS for `N <= 7`.
