# 03 - TreeLongestZigZag

**Codility:** [TreeLongestZigZag](https://app.codility.com/programmers/trainings/7/tree_longest_zig_zag/) - Exercise 7, Data Structures - *medium*

Given a tree, find a downward path with the maximal number of direction changes.

## Task description

In this problem we consider binary trees. Let's define a *turn* on a path as a change in the direction of the path (i.e. a switch from right to left or vice versa). A *zigzag* is simply a sequence of turns (it can start with either right or left). The *length* of a zigzag is equal to the number of turns.

Consider this binary tree (written as `(value, left, right)`):

```
(5,
  (3, (20, (6, None, None), None), None),
  (10,
    (1, None, None),
    (15, (30, None, (9, None, None)), (8, None, None))))
```

The path `5 -> 10 -> 15 -> 30 -> 9` (right, right, left, right) has two turns: the first at `15`, the second at `30`. The length of this zigzag is 2. This is also the longest zigzag in the tree.

In this problem you should find the longest zigzag that **starts at the root** of any given binary tree and forms a **downwards path**.

Note that a zigzag containing only one edge or one node has length `0`.

### Problem

Write a function:

```python
def solution(T)
```

that, given a non-empty binary tree `T` consisting of `N` nodes, returns the length of the longest zigzag starting at the root.

For the tree above the function should return `2`. The values contained in the nodes are not relevant in this task.

### Technical details

A binary tree is specified using a pointer data structure. The following declaration is given:

```python
from dataclasses import dataclass, field

@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None
```

An empty tree is represented by `None`. A non-empty tree is represented by an object representing its root. The attribute `x` holds the integer contained in the root, whereas `l` and `r` hold the left and right subtrees.

To enter your own test cases, a tree can be denoted recursively as `(X, L, R)`, with `None` for an empty tree.

### Assumptions

- `N` is an integer within the range `[1..100,000]`;
- the height of tree `T` (number of edges on the longest path from root to leaf) is within the range `[0..800]`.

Write an **efficient** algorithm.

## Files

| File                            | Purpose                                                              |
|---------------------------------|----------------------------------------------------------------------|
| `README.md`                     | This description.                                                    |
| `requirements.txt`              | Dependencies of this mini-project.                                   |
| `tree_longest_zig_zag.ipynb`    | Solution, tree parser, edge cases, brute-force check and large trees. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_7_data_structures/03_tree_longest_zig_zag/requirements.txt
jupyter lab codility/exercise_7_data_structures/03_tree_longest_zig_zag/tree_longest_zig_zag.ipynb
```

## Hints

1. For each node keep two numbers: the best number of turns for a path that **arrived** at the node going left, and the same for a path that arrived going right.
2. At a node reached by a *left* edge: continuing left costs nothing (`best_left(l)`), switching to the right child adds one turn (`1 + best_right(r)`); stopping gives 0. The mirror rule applies for a node reached by a right edge.
3. At the root there is no previous direction, so the first edge never counts as a turn: the answer is `max(best_left(l), best_right(r))`, or `0` for a single node.
4. The height is at most 800 and Python's default recursion limit is 1000, so a recursive solution barely fits (helper frames and the test harness also count). An **iterative post-order** traversal with an explicit stack avoids the risk.
5. Complexity: O(N) time, O(N) space.
