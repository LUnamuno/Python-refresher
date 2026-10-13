# 02 - FloodDepth

**Codility:** [FloodDepth](https://app.codility.com/programmers/trainings/1/flood_depth/) - Exercise 1, 2015 Contest

Maximum depth of water held by a one-dimensional landscape after a flood.

## Task description

You are helping a geologist friend investigate an area with mountain lakes. A recent heavy rainfall has flooded these lakes and their water levels have reached the highest possible point. Your friend is interested to know the maximum depth in the deepest part of these lakes.

We simplify the problem in 2-D dimensions. The whole landscape can be divided into small blocks and described by an array `A` of length `N`. Each element of `A` is the altitude of the rock floor of a block (i.e. the height of this block when there is no water at all). After the rainfall, all the low-lying areas (i.e. blocks that have higher blocks on both sides) are holding as much water as possible. You would like to know the maximum depth of water after this entire area is flooded. You can assume that the altitude outside this area is zero and the outside area can accommodate infinite amount of water.

For example, consider array `A` such that:

```
A[0] = 1    A[1] = 3    A[2] = 2    A[3] = 1    A[4] = 2    A[5] = 1
A[6] = 5    A[7] = 3    A[8] = 3    A[9] = 4    A[10] = 2
```

The original statement shows a picture of the landscape after it has flooded (rock floor in gray, water in blue). Thus, blocks 3 and 5 have a water depth of 2 while blocks 2, 4, 7 and 8 have a water depth of 1. Therefore, the maximum water depth of this area is 2.

Write a function:

```python
def solution(A)
```

that, given a non-empty array `A` consisting of `N` integers, returns the maximum depth of water.

Given array `A` shown above, the function should return `2`, as explained above.

For the array `A = [5, 8]` the function should return `0`, because this landscape cannot hold any water.

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- each element of array `A` is an integer within the range `[1..100,000,000]`.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `flood_depth.ipynb` | Prefix/suffix maxima solution, official examples, relaxation reference and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_1_2015_contest/02_flood_depth/requirements.txt
jupyter lab codility/exercise_1_2015_contest/02_flood_depth/flood_depth.ipynb
```

## Hints

1. The water level above block `i` is limited by the highest block to its left and the highest block to its right: `level[i] = min(max(A[0..i]), max(A[i..N-1]))`.
2. The depth is `level[i] - A[i]`, and the answer is the maximum over `i`. Including `A[i]` in both maxima makes the depth automatically `>= 0`.
3. The outside has altitude 0 and drains everything, which is why the first and last blocks never hold water (their maximum on one side is themselves).
4. Compute the prefix and suffix maxima in two passes. Complexity: O(N) time, O(N) space.
