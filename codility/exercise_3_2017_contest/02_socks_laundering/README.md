# 02 - SocksLaundering

**Codility:** [SocksLaundering](https://app.codility.com/programmers/trainings/3/socks_laundering/) - Exercise 3, 2017 Contest

Pick dirty socks to wash so that the number of same-colour pairs is maximal.

## Task description

Bob is about to go on a trip. But first he needs to take care of his supply of socks. Each sock has its own color. Bob wants to take as many pairs of clean socks as possible (both socks in the pair should be of the same color).

Socks are divided into two drawers: clean and dirty socks. Bob has time for only one laundry and his washing machine can clean at most `K` socks. He wants to pick socks for laundering in such a way that after washing he will have a maximal number of clean, same-colored pairs of socks. It is possible that some socks cannot be paired with any other sock, because Bob may have lost some socks over the years.

Bob has exactly `N` clean and `M` dirty socks, which are described in arrays `C` and `D`, respectively. The colors of the socks are represented as integers (equal numbers representing identical colors).

For example, given four clean socks and five dirty socks (the original statement shows a picture; the colors are `C = [1, 2, 1, 1]` and `D = [1, 4, 3, 2, 4]`):

If Bob's washing machine can clean at most `K = 2` socks, then he can take a maximum of three pairs of clean socks. He can wash one sock of color 1 and one sock of color 2 (both from the dirty drawer). Then he will have two pairs of color 1 and one pair of color 2.

Write a function:

```python
def solution(K, C, D)
```

that, given an integer `K` (the number of socks that the washing machine can clean), two arrays `C` and `D` (containing the color representations of `N` clean and `M` dirty socks respectively), returns the maximum number of pairs of socks that Bob can take on the trip.

For example, given `K = 2`, `C = [1, 2, 1, 1]` and `D = [1, 4, 3, 2, 4]`, the function should return `3`, as explained above.

### Assumptions

- `K` is an integer within the range `[0..50]`;
- each element of arrays `C` and `D` is an integer within the range `[1..50]`;
- `C` and `D` are not empty and each of them contains at most 50 elements.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `socks_laundering.ipynb` | Greedy solution, official example, brute-force check and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_3_2017_contest/02_socks_laundering/requirements.txt
jupyter lab codility/exercise_3_2017_contest/02_socks_laundering/socks_laundering.ipynb
```

## Hints

1. Pairs are per colour: a colour with `n` clean socks already gives `n // 2` pairs.
2. A colour with an **odd** number of clean socks has one lonely sock: washing **one** dirty sock of that colour creates a new pair. That is the cheapest improvement (1 sock per pair).
3. After that, the remaining capacity can wash two dirty socks of the same colour at a time (2 socks per pair).
4. Greedy: first spend washes on the single socks (at most `K`), then spend the rest on dirty pairs: `min(remaining // 2, available dirty pairs)`.
5. Careful with a colour that is odd in the clean drawer: once its single dirty sock is used, only `dirty - 1` socks are left to form pairs.
