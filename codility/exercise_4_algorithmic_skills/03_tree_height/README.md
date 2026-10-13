# 03 - TreeHeight

**Codility:** [TreeHeight](https://app.codility.com/programmers/trainings/4/tree_height/) - Exercise 4, Algorithmic skills

Compute the height of a binary tree.

## Task description

In this problem we consider binary trees, represented by pointer data structures.

A binary tree is either an empty tree or a node (called the root) consisting of a single integer value and two further binary trees, called the left subtree and the right subtree.

For example, this binary tree (written as `(value, left, right)`) has six nodes:

```
(5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None))
```

Its root contains the value 5, and the roots of its left and right subtrees have the values 3 and 10. The right subtree of the node with value 10, as well as the left and right subtrees of the nodes with values 20, 21 and 1, are empty trees.

A *path* in a binary tree is a non-empty sequence of nodes that one can traverse by following the pointers. The *length* of a path is the number of pointers it traverses. For example, the sequence of nodes with values `5, 3, 21` is a path of length 2. The sequence `10, 1` is a path of length 1. The sequence `21, 3, 20` is not a valid path.

The *height* of a binary tree is defined as the length of the longest possible path in the tree. In particular, a tree consisting of only one node has height `0` and, conventionally, an empty tree has height `-1`. The tree above has height `2`.

### Problem

Write a function:

```python
def solution(T)
```

that, given a non-empty binary tree `T` consisting of `N` nodes, returns its height. For the tree above the function should return `2`. The values contained in the nodes are not relevant in this task.

### Technical details

A binary tree is given using a pointer data structure:

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

- `N` is an integer within the range `[1..1,000]`;
- the height of tree `T` (number of edges on the longest path from root to leaf) is within the range `[0..500]`.

Write an **efficient** algorithm.

## Files

| File                  | Purpose                                                              |
|-----------------------|----------------------------------------------------------------------|
| `README.md`           | This description.                                                    |
| `requirements.txt`    | Dependencies of this mini-project.                                   |
| `tree_height.ipynb`   | Recursive and iterative solutions, tree parser, brute-force check.   |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/03_tree_height/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/03_tree_height/tree_height.ipynb
```

## Hints

1. Recursive definition: `height(None) = -1` and `height(node) = 1 + max(height(node.l), height(node.r))`. That reproduces the conventions of the statement (a leaf has height 0).
2. The height can reach 500; Python's default recursion limit is 1000. A recursive solution fits, but an **iterative** one (level-by-level BFS with a list or `deque`) has no such limit.
3. BFS version: count how many levels the tree has and subtract 1.
4. Complexity: O(N) time, O(N) space in the worst case.
