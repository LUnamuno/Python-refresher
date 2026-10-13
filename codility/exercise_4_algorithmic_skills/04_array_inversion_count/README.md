# 04 - ArrayInversionCount

**Codility:** [ArrayInversionCount](https://app.codility.com/programmers/trainings/4/array_inversion_count/) - Exercise 4, Algorithmic skills

Count the inversions of an array.

## Task description

An array `A` consisting of `N` integers is given. An *inversion* is a pair of indexes `(P, Q)` such that `P < Q` and `A[Q] < A[P]`.

Write a function:

```python
def solution(A)
```

that computes the number of inversions in `A`, or returns `-1` if it exceeds `1,000,000,000`.

For example, in the following array:

```
A[0] = -1  A[1] = 6  A[2] = 3
A[3] =  4  A[4] = 7  A[5] = 4
```

there are four inversions: `(1,2)`, `(1,3)`, `(1,5)` and `(4,5)`, so the function should return `4`.

### Assumptions

- `N` is an integer within the range `[0..100,000]`;
- each element of array `A` is an integer within the range `[-2,147,483,648..2,147,483,647]`.

Write an **efficient** algorithm.

## Files

| File                            | Purpose                                                                    |
|---------------------------------|----------------------------------------------------------------------------|
| `README.md`                     | This description.                                                          |
| `requirements.txt`              | Dependencies of this mini-project.                                         |
| `array_inversion_count.ipynb`   | Merge-sort solution, Fenwick-tree cross-check, brute force and boundary tests. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/04_array_inversion_count/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/04_array_inversion_count/array_inversion_count.ipynb
```

## Hints

1. Brute force over all pairs is O(N^2): about `5 * 10^9` pairs for `N = 100,000`. Too slow.
2. **Merge sort counting:** while merging two sorted halves, every time you take an element from the *right* half before the remaining elements of the *left* half, it forms an inversion with each of those remaining left elements.
3. Equal elements are **not** inversions (`A[Q] < A[P]` is strict), so on ties take the left element first.
4. Alternative: a **Fenwick tree** (binary indexed tree) over compressed values counting, for each element, how many earlier elements are greater.
5. The empty array (`N = 0`) has `0` inversions.
6. The count can reach `N(N-1)/2`, about `5 * 10^9`: compare with `1,000,000,000` and return `-1` when it is exceeded (Python integers do not overflow, so this is only a matter of following the statement).
7. Complexity: O(N log N) time, O(N) space.
