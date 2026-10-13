# 01 - ParkingBill

**Codility:** [ParkingBill](https://app.codility.com/programmers/trainings/5/parking_bill/) - Exercise 5, Coding skills - *elementary*

Given two strings representing times of entry and exit from a car parking lot, find the cost of the ticket according to the given billing rules.

## Task description

You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:

- The entrance fee of the car parking lot is `2`;
- The first full or partial hour costs `3`;
- Each successive full or partial hour (after the first) costs `4`.

You entered the car parking lot at time `E` and left at time `L`. In this task, times are represented as strings in the format `"HH:MM"` (where `HH` is a two-digit number between 0 and 23, which stands for hours, and `MM` is a two-digit number between 0 and 59, which stands for minutes).

Write a function:

```python
def solution(E, L)
```

that, given strings `E` and `L` specifying points in time in the format `"HH:MM"`, returns the total cost of the parking bill from your entry at time `E` to your exit at time `L`. You can assume that `E` describes a time before `L` on the same day.

Examples:

| E       | L       | result | why                                                                  |
|---------|---------|--------|----------------------------------------------------------------------|
| `10:00` | `13:21` | 17     | `2 + 3 + (3 * 4)`: entrance, first hour, two full hours and a partial one |
| `09:42` | `11:42` | 9      | `2 + 3 + 4`: entrance, first hour, second hour                       |

### Assumptions

- strings `E` and `L` follow the format `"HH:MM"` strictly;
- string `E` describes a time before `L` on the same day.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File                  | Purpose                                                             |
|-----------------------|---------------------------------------------------------------------|
| `README.md`           | This description.                                                   |
| `requirements.txt`    | Dependencies of this mini-project.                                  |
| `parking_bill.ipynb`  | Solution, official examples, edge cases and a simulation reference. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_5_coding_skills/01_parking_bill/requirements.txt
jupyter lab codility/exercise_5_coding_skills/01_parking_bill/parking_bill.ipynb
```

## Hints

1. Convert both times to **minutes since midnight** (`HH * 60 + MM`); the stay is the difference.
2. Count billed hours as a **ceiling division**: `ceil(minutes / 60)`. With integers: `(minutes + 59) // 60` or `-(-minutes // 60)`.
3. The first hour costs 3, every other billed hour costs 4: `2 + 3 + 4 * (hours - 1)`.
4. Boundaries: exactly 60 minutes is **one** hour, 61 minutes is **two**. Because `E < L`, the stay is at least one minute, so there is always at least one billed hour.
5. Complexity: O(1).
