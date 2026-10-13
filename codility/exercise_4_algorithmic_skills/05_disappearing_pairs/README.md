# 05 - DisappearingPairs

**Codility:** [DisappearingPairs](https://app.codility.com/programmers/trainings/4/disappearing_pairs/) - Exercise 4, Algorithmic skills

Repeatedly remove equal adjacent letters from a string over `A`, `B`, `C`.

## Task description

A string `S` containing only the letters `"A"`, `"B"` and `"C"` is given. The string can be transformed by removing one occurrence of `"AA"`, `"BB"` or `"CC"`.

*Transformation* of the string is the process of removing letters from it, based on the rules described above. As long as at least one rule can be applied, the process should be repeated. If more than one rule can be used, any one of them could be chosen.

Write a function:

```python
def solution(S)
```

that, given a string `S` consisting of `N` characters, returns any string that can result from a sequence of transformations as described above.

Examples:

- Given `S = "ACCAABBC"` the function may return `"AC"`, because one of the possible sequences of transformations is:
  `ACCAABBC -> AAABBC -> ABBC -> AC`.
- Given `S = "ABCBBCBA"` the function may return `""`, because one possible sequence is:
  `ABCBBCBA -> ABCCBA -> ABBA -> AA -> ""`.
- Given `S = "BABABA"` the function must return `"BABABA"`, because no rules can be applied to string `S`.

### Assumptions

- the length of string `S` is within the range `[0..50,000]`;
- string `S` is made only of the following characters: `'A'`, `'B'` and/or `'C'`.

Write an **efficient** algorithm.

## Files

| File                          | Purpose                                                              |
|-------------------------------|----------------------------------------------------------------------|
| `README.md`                   | This description.                                                    |
| `requirements.txt`            | Dependencies of this mini-project.                                   |
| `disappearing_pairs.ipynb`    | Stack solution, exhaustive search of all reduction orders, large inputs. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/05_disappearing_pairs/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/05_disappearing_pairs/disappearing_pairs.ipynb
```

## Hints

1. Process the string left to right with a **stack**: if the new letter equals the top of the stack, pop (they cancel); otherwise push.
2. The stack always holds a string with no adjacent equal letters, so at the end no rule can be applied.
3. The statement says "any" result, but the final string is actually **unique**: whatever order of removals you choose, you end at the same irreducible string. The notebook verifies this by brute force.
4. Naively searching for `"AA"`, `"BB"` or `"CC"` and rebuilding the string after every removal is O(N^2) in the worst case.
5. Complexity: O(N) time, O(N) space.
