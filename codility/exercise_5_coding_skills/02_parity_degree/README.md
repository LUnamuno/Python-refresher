# 02 - ParityDegree

**Codility:** [ParityDegree](https://app.codility.com/programmers/trainings/5/parity_degree/) - Exercise 5, Coding skills - *easy*

Find the highest power of 2 that divides `N`.

## Task description

A positive integer `N` is given. The goal is to find the highest power of 2 that divides `N`. In other words, we have to find the maximum `K` for which `N modulo 2^K` is `0`.

For example, given integer `N = 24` the answer is `3`, because `2^3 = 8` is the highest power of 2 that divides `N`.

Write a function:

```python
def solution(N)
```

that, given a positive integer `N`, returns the highest power of 2 that divides `N` (that is, the exponent `K`).

For `N = 24` the function should return `3`, as explained above.

### Assumptions

- `N` is an integer within the range `[1..1,000,000,000]`.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File                    | Purpose                                                           |
|-------------------------|-------------------------------------------------------------------|
| `README.md`             | This description.                                                 |
| `requirements.txt`      | Dependencies of this mini-project.                                |
| `parity_degree.ipynb`   | Solutions, official example, edge cases and a check against the definition. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_5_coding_skills/02_parity_degree/requirements.txt
jupyter lab codility/exercise_5_coding_skills/02_parity_degree/parity_degree.ipynb
```

## Hints

1. The answer is the exponent of 2 in the prime factorisation of `N`: how many times can you divide `N` by 2 while it stays an integer?
2. Simple loop: `while N % 2 == 0: N //= 2; count += 1`. It runs at most about 30 times for `N <= 10^9`.
3. Bit trick: `N & -N` isolates the lowest set bit (a power of two `2^K`), and `(N & -N).bit_length() - 1` is `K`. In binary, `K` is the number of trailing zeros of `N`.
4. `24 = 11000` in binary has three trailing zeros, so the answer is 3.
5. Complexity: O(log N) for the loop, O(1) for the bit trick.
