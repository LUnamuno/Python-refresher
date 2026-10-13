# 01 - FirstUnique

**Codility:** [FirstUnique](https://app.codility.com/programmers/trainings/4/first_unique/) - Exercise 4, Algorithmic skills

Find the first number that occurs exactly once in an array.

## Task description

A non-empty array `A` consisting of `N` integers is given. The *unique number* is the number that occurs exactly once in array `A`.

For example, the following array `A`:

```
A[0] = 4
A[1] = 10
A[2] = 5
A[3] = 4
A[4] = 2
A[5] = 10
```

contains two unique numbers (`5` and `2`).

You should find the **first unique number** in `A`. In other words, find the unique number with the lowest position in `A`.

For the example above, `5` is at index 2 (`A[2] = 5`) and `2` is at index 4 (`A[4] = 2`). So the first unique number is `5`.

Write a function:

```python
def solution(A)
```

that, given a non-empty array `A` of `N` integers, returns the first unique number in `A`. The function should return `-1` if there are no unique numbers in `A`.

For example, given `A = [1, 4, 3, 3, 1, 2]` the function should return `4`. There are two unique numbers (`4` and `2` occur exactly once); the first one is `4` at index 1 and the second is `2` at index 5, so it returns `4`.

Given `A = [6, 4, 4, 6]` the function should return `-1`: there is no unique number (`4` and `6` occur more than once).

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- each element of array `A` is an integer within the range `[0..1,000,000,000]`.

Write an **efficient** algorithm.

## Files

| File                  | Purpose                                                       |
|-----------------------|---------------------------------------------------------------|
| `README.md`           | This description.                                             |
| `requirements.txt`    | Dependencies of this mini-project.                            |
| `first_unique.ipynb`  | Solution, official examples, edge cases, brute force and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/01_first_unique/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/01_first_unique/first_unique.ipynb
```

## Hints

1. Counting problem: first pass counts occurrences (`collections.Counter` or a `dict`), second pass returns the first element whose count is 1.
2. Do **not** call `A.count(x)` inside a loop: that is O(N^2) and too slow for `N = 100,000`.
3. The function returns the **value**, not its index. Since values are in `[0..10^9]`, `-1` is a safe "not found" marker.
4. Complexity: O(N) time, O(N) space.
