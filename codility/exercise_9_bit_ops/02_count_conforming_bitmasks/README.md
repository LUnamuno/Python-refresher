# 02 - CountConformingBitmasks

**Codility:** [CountConformingBitmasks](https://app.codility.com/programmers/trainings/9/count_conforming_bitmasks/) - Exercise 9, Bitwise operations - *medium*

Count 30-bit bitmasks conforming to at least one of three given 30-bit bitmasks.

## Task description

In this problem we consider unsigned 30-bit integers, i.e. all integers `B` such that `0 <= B < 2**30`.

We say that integer `A` *conforms* to integer `B` if, in all positions where `B` has bits set to 1, `A` has corresponding bits set to 1.

For example:

- `00 0000 1111 0111 1101 1110 0000 1111` (BIN) = 16,244,239 conforms to `00 0000 1100 0110 1101 1110 0000 0001` (BIN) = 13,032,961, but
- `11 0000 1101 0111 0000 1010 0000 0101` (BIN) = 819,399,173 does **not** conform to `00 0000 1001 0110 0011 0011 0000 1111` (BIN) = 9,843,471.

Write a function:

```python
def solution(A, B, C)
```

that, given three unsigned 30-bit integers `A`, `B` and `C`, returns the number of unsigned 30-bit integers conforming to at least one of the given integers.

For example, for integers:

```
A = 11 1111 1111 1111 1111 1111 1001 1111 (BIN) = 1,073,741,727
B = 11 1111 1111 1111 1111 1111 0011 1111 (BIN) = 1,073,741,631
C = 11 1111 1111 1111 1111 1111 0110 1111 (BIN) = 1,073,741,679
```

the function should return `8`, since there are 8 unsigned 30-bit integers conforming to `A`, `B` or `C`, namely:

```
1,073,741,631  1,073,741,679  1,073,741,695  1,073,741,727
1,073,741,759  1,073,741,791  1,073,741,807  1,073,741,823
```

### Assumptions

- `A`, `B` and `C` are integers within the range `[0..1,073,741,823]`.

Write an **efficient** algorithm: iterating over all `2**30` candidates is far too slow.

## Files

| File                              | Purpose                                                          |
|-----------------------------------|------------------------------------------------------------------|
| `README.md`                       | This description.                                                |
| `requirements.txt`                | Dependencies of this mini-project.                               |
| `count_conforming_bitmasks.ipynb` | Solution, official example, edge cases and a brute-force check.  |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_9_bit_ops/02_count_conforming_bitmasks/requirements.txt
jupyter lab codility/exercise_9_bit_ops/02_count_conforming_bitmasks/count_conforming_bitmasks.ipynb
```

## Hints

1. How many integers conform to a single mask `X`? The bits set in `X` are forced to 1; the remaining `30 - popcount(X)` bits are free, so `2 ** (30 - popcount(X))`.
2. The sets of conformers of `A`, `B` and `C` overlap. Use **inclusion-exclusion**.
3. An integer conforms to both `X` and `Y` exactly when it conforms to `X | Y` (it must have every bit of either mask set).
4. Therefore: `f(A) + f(B) + f(C) - f(A|B) - f(A|C) - f(B|C) + f(A|B|C)`, where `f(X) = 2 ** (30 - popcount(X))`.
5. Check with the example: `4 + 4 + 4 - 2 - 1 - 2 + 1 = 8`.
6. Complexity: O(1) time and space.
