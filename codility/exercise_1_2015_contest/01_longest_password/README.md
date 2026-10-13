# 01 - LongestPassword

**Codility:** [LongestPassword](https://app.codility.com/programmers/trainings/1/longest_password/) - Exercise 1, 2015 Contest

Length of the longest word of a sentence that is a valid password.

## Task description

You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

- it has to contain only alphanumerical characters (`a-z`, `A-Z`, `0-9`);
- there should be an even number of letters;
- there should be an odd number of digits.

You are given a string `S` consisting of `N` characters. String `S` can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are `K` spaces in string `S` then there are exactly `K + 1` words.

For example, given `"test 5 a0A pass007 ?xy1"`, there are five words and three of them are valid passwords: `"5"`, `"a0A"` and `"pass007"`. Thus the longest password is `"pass007"` and its length is 7. Note that neither `"test"` nor `"?xy1"` is a valid password, because `"?"` is not an alphanumerical character and `"test"` contains an even number of digits (zero).

Write a function:

```python
def solution(S)
```

that, given a non-empty string `S` consisting of `N` characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return `-1`.

For example, given `S = "test 5 a0A pass007 ?xy1"`, your function should return `7`, as explained above.

### Assumptions

- `N` is an integer within the range `[1..200]`;
- string `S` consists only of printable ASCII characters and spaces.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `longest_password.ipynb` | Solution, official example, regex reference and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_1_2015_contest/01_longest_password/requirements.txt
jupyter lab codility/exercise_1_2015_contest/01_longest_password/longest_password.ipynb
```

## Hints

1. `S.split(" ")` gives exactly `K + 1` words for `K` spaces (empty words appear when there are consecutive spaces; they are never valid).
2. A word is valid when all its characters are in `a-z`, `A-Z` or `0-9` **and** the number of letters is even **and** the number of digits is odd.
3. Be careful with `str.isalnum()`: it also accepts non-ASCII letters (for example `"e"` with an accent). An explicit ASCII check is stricter and safer.
4. Keep the maximum length of the valid words, or `-1`. Complexity: O(N).
