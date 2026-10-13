# 01 - TennisTournament

**Codility:** [TennisTournament](https://app.codility.com/programmers/trainings/3/tennis_tournament/) - Exercise 3, 2017 Contest

Maximum number of tennis games that can start at the same time.

## Task description

You are hosting a tennis tournament. `P` players, who will take part in the first round of this tournament, are already registered and you have reserved `C` tennis courts for the matches. Exactly two players play in each game and only one game can be played on each court at any given time. You want to host the maximum possible number of games starting at the same time (in order to finish the first round quickly).

How many games can be hosted in parallel simultaneously?

Write a function:

```python
def solution(P, C)
```

that, given the number of players `P` and the number of reserved courts `C`, returns the maximum number of games that can be played in parallel.

### Examples

1. Given `P = 5` players and `C = 3` available courts, the function should return `2`. Two games can be played simultaneously (for instance, the first and second players can play on the first court, and the third and fourth players on the second court, and the third court will be empty because the fifth player does not have a partner to play with).
2. Given `P = 10` players and `C = 3` courts, the function should return `3`. At most three games can be hosted in parallel.

### Assumptions

- `P` and `C` are integers within the range `[1..30,000]`.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `tennis_tournament.ipynb` | Solution, official examples, exhaustive check and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_3_2017_contest/01_tennis_tournament/requirements.txt
jupyter lab codility/exercise_3_2017_contest/01_tennis_tournament/tennis_tournament.ipynb
```

## Hints

1. Two limits apply at the same time: the players (each game needs two) and the courts (one game per court).
2. With `P` players at most `P // 2` games can be formed (integer division: the odd player has no partner).
3. With `C` courts at most `C` games fit at the same time.
4. The answer is the smaller of the two limits: `min(P // 2, C)`. Complexity: O(1).
