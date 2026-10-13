# 01 - BinaryGap

**Codility:** [BinaryGap](https://app.codility.com/programmers/trainings/9/binary_gap/) - Exercise 9, Bitwise operations - *easy*

Find the longest sequence of zeros in the binary representation of an integer.

## Task description

A *binary gap* within a positive integer `N` is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of `N`.

For example:

- `9` has binary representation `1001` and contains a binary gap of length 2.
- `529` has binary representation `1000010001` and contains two binary gaps: one of length 4 and one of length 3.
- `20` has binary representation `10100` and contains one binary gap of length 1.
- `15` has binary representation `1111` and has no binary gaps.
- `32` has binary representation `100000` and has no binary gaps (the zeros are not closed by a one on the right).

Write a function:

```python
def solution(N)
```

that, given a positive integer `N`, returns the length of its longest binary gap. The function should return `0` if `N` does not contain a binary gap.

Examples:

| N    | binary        | result |
|------|---------------|--------|
| 1041 | `10000010001` | 5      |
| 32   | `100000`      | 0      |
| 529  | `1000010001`  | 4      |

### Assumptions

- `N` is an integer within the range `[1..2,147,483,647]`.

Write an **efficient** algorithm.

## Files

| File                | Purpose                                                        |
|---------------------|----------------------------------------------------------------|
| `README.md`         | This description.                                              |
| `requirements.txt`  | Dependencies of this mini-project.                             |
| `binary_gap.ipynb`  | Solution, official examples, edge cases and a brute-force check. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_9_bit_ops/01_binary_gap/requirements.txt
jupyter lab codility/exercise_9_bit_ops/01_binary_gap/binary_gap.ipynb
```

## Hints

1. `bin(N)` returns a string such as `'0b1001'`; strip the `0b` prefix.
2. Trailing zeros are *not* part of a gap (no `1` on their right). Leading zeros do not exist in `bin()`.
3. Two approaches: split the string on `'1'`, or scan the bits keeping a counter of the current run of zeros.
4. Complexity: O(log N) time (about 31 bits), O(1) extra space for the bit-scan version.
