# 01 - ArrListLen

**Codility:** [ArrListLen](https://app.codility.com/programmers/trainings/7/arr_list_len/) - Exercise 7, Data Structures - *easy*

Compute the length of a single-link list encoded in an array.

## Task description

A non-empty array `A` consisting of `N` integers is given.

Array `A` represents a linked list. A list is constructed from this array as follows:

- the first node (the head) is located at index `0`;
- the value of a node located at index `K` is `A[K]`;
- if the value of a node is `-1` then it is the last node of the list;
- otherwise, the successor of a node located at index `K` is located at index `A[K]` (you can assume that `A[K]` is a valid index, that is `0 <= A[K] < N`).

For example, for array `A` such that:

```
A[0] =  1
A[1] =  4
A[2] = -1
A[3] =  3
A[4] =  2
```

the following list is constructed:

- the first node (the head) is located at index 0 and has a value of 1;
- the second node is located at index 1 and has a value of 4;
- the third node is located at index 4 and has a value of 2;
- the fourth node is located at index 2 and has a value of -1.

Write a function:

```python
def solution(A)
```

that, given a non-empty array `A` consisting of `N` integers, returns the length of the list constructed from `A` in the above manner.

For the array above the function should return `4`.

### Assumptions

- `N` is an integer within the range `[1..200,000]`;
- each element of array `A` is an integer within the range `[-1..N-1]`;
- it will always be possible to construct the list and its length will be finite.

In your solution, focus on **correctness**. The performance of your solution will not be the focus of the assessment.

## Files

| File                  | Purpose                                                         |
|-----------------------|-----------------------------------------------------------------|
| `README.md`           | This description.                                               |
| `requirements.txt`    | Dependencies of this mini-project.                              |
| `arr_list_len.ipynb`  | Solution, official example, edge cases and a reference check.   |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_7_data_structures/01_arr_list_len/requirements.txt
jupyter lab codility/exercise_7_data_structures/01_arr_list_len/arr_list_len.ipynb
```

## Hints

1. Walk the list: start at index `0`, count the node, jump to `A[index]`, stop when the value is `-1`.
2. The last node (value `-1`) **is** counted: in the example the nodes are at indices `0, 1, 4, 2`, so the length is 4.
3. The statement guarantees the list is finite, so there are no cycles to detect.
4. Complexity: O(N) time, O(1) extra space.
