# 02 - StrSymmetryPoint

**Codility:** [StrSymmetryPoint](https://app.codility.com/programmers/trainings/4/str_symmetry_point/) - Exercise 4, Algorithmic skills

Find the index of the character at the centre of a string whose two sides mirror each other.

## Task description

Write a function:

```python
def solution(S)
```

that, given a string `S`, returns the index (counting from 0) of a character such that the part of the string to the left of that character is a reversal of the part of the string to its right. The function should return `-1` if no such index exists.

Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

For example, given the string `"racecar"` the function should return `3`, because the substring to the left of the character `"e"` at index 3 is `"rac"`, and the one to the right is `"car"`.

Given the string `"x"` the function should return `0`, because both substrings are empty.

### Assumptions

- the length of string `S` is within the range `[0..2,000,000]`.

Write an **efficient** algorithm.

## Files

| File                          | Purpose                                                       |
|-------------------------------|---------------------------------------------------------------|
| `README.md`                   | This description.                                             |
| `requirements.txt`            | Dependencies of this mini-project.                            |
| `str_symmetry_point.ipynb`    | Solution, official examples, edge cases, brute force and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/02_str_symmetry_point/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/02_str_symmetry_point/str_symmetry_point.ipynb
```

## Hints

1. Only the **middle** character can have equal-length halves, so there is at most one candidate: index `len(S) // 2`, and only when `len(S)` is odd.
2. If the length is even, no character has equal halves: return `-1`. This also covers the empty string, which has no character at all.
3. For an odd length, the answer is the middle index if and only if the whole string is a **palindrome** (`S == S[::-1]`).
4. Trying every index and comparing slices is O(N^2) and fails for `N = 2,000,000`.
5. Complexity: O(N) time, O(N) extra space for the reversed copy (or O(1) with a two-pointer comparison).
