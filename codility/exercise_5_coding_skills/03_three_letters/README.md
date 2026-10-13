# 03 - ThreeLetters

**Codility:** [ThreeLetters](https://app.codility.com/programmers/trainings/5/three_letters/) - Exercise 5, Coding skills - *medium*

Given two integers `A` and `B`, return a string which contains `A` letters `a` and `B` letters `b` with no three consecutive letters being the same.

## Task description

Write a function `solution` that, given two integers `A` and `B`, returns a string containing exactly `A` letters `'a'` and exactly `B` letters `'b'` with no three consecutive letters being the same (in other words, neither `"aaa"` nor `"bbb"` may occur in the returned string).

```python
def solution(A, B)
```

Examples:

1. Given `A = 5` and `B = 3`, your function may return `"aabaabab"`. Note that `"abaabbaa"` would also be a correct answer. Your function may return **any** correct answer.
2. Given `A = 3` and `B = 3`, your function should return `"ababab"`, `"aababb"`, `"abaabb"` or any of several other strings.
3. Given `A = 1` and `B = 4`, your function should return `"bbabb"`, which is the only correct answer in this case.

### Assumptions

- `A` and `B` are integers within the range `[0..100]`;
- at least one solution exists for the given `A` and `B`.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File                    | Purpose                                                                  |
|-------------------------|--------------------------------------------------------------------------|
| `README.md`             | This description.                                                        |
| `requirements.txt`      | Dependencies of this mini-project.                                       |
| `three_letters.ipynb`   | Greedy solution, validator, exhaustive checks of every `(A, B)` in range. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_5_coding_skills/03_three_letters/requirements.txt
jupyter lab codility/exercise_5_coding_skills/03_three_letters/three_letters.ipynb
```

## Hints

1. Many answers are valid, so test with a **validator** (right counts, no `"aaa"`, no `"bbb"`) instead of comparing with one string.
2. Greedy idea: always place the letter with more copies left, **unless** that would create three in a row (the last two letters are already that letter); then place the other one.
3. When does a solution exist at all? The `B` letters `b` split the string into `B + 1` slots for runs of `a`, each of length at most 2, so `A <= 2 * (B + 1)`; symmetrically `B <= 2 * (A + 1)`.
4. Check `(1, 4)`: greedy gives `b b a b b`, the only valid string.
5. Complexity: O(A + B).
