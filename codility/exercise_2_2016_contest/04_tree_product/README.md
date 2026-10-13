# 04 - TreeProduct

**Codility:** [TreeProduct](https://app.codility.com/programmers/trainings/2/tree_product/) - Exercise 2, 2016 Contest

Cut at most two edges of a tree to maximise the product of the component sizes.

## Task description

Elves in the forest of Glandishar are preparing for an Orc invasion. They have a network of `N + 1` guard posts located on the open platforms in the treetops. The posts are numbered from 0 to `N` and are connected by `N` bridges, so that one can get from any one guard post to any other guard post in a unique way. In other words, guard posts and bridges form a tree graph.

The Elves are afraid that if the Orcs manage to get hold of one of the guard posts, then they will have easy access to all the other guard posts. Therefore, the Elves have decided to destroy at most two bridges and split the guard posts into at most three separate areas, so that the guards can move within each area but it's not possible to move between the areas.

In each area there will be one guard who will move from guard post to guard post during the night. If the Orcs attack, the guards will raise an alarm. However, if the Orcs manage to guess the guard post in which the guards are currently located, they may manage to take out the guards without raising the alarm. The Elves want to avoid the situation that all guard posts fail this way, by maximizing:

- `X * Y * Z`, if the guard posts have been divided into three areas consisting of `X`, `Y` and `Z` guard posts, respectively;
- `X * Y`, if the guard posts have been divided into two areas consisting of `X` and `Y` posts, respectively;
- `N + 1`, if the guard posts haven't been divided;

depending on which option gives the largest result.

You are given a map of the network in the form of two arrays `A`, `B` of length `N`. For each `K` (`0 <= K < N`) there is a bridge between posts `A[K]` and `B[K]`.

Write a function:

```python
def solution(A, B)
```

that, given two arrays `A` and `B` of `N` integers, returns the largest possible result. Since the result can be large, you should return it as a **string**.

### Examples

1. Given `A = [0, 1, 1, 3, 3, 6, 7]` and `B = [1, 2, 3, 4, 5, 3, 5]` (bridges `0-1`, `1-2`, `1-3`, `3-4`, `3-5`, `6-3`, `7-5`) the function should return `"18"` since the Elves can destroy bridges `1-3` and `3-5`. The created areas consist of 3, 3 and 2 guard posts. Therefore, the result is `3 * 3 * 2 = 18`. It is not possible to obtain a better result.
2. Given `A = [0, 1]` and `B = [1, 2]` the function should return `"3"` (it is optimal not to destroy any bridge).

### Assumptions

- `N` is an integer within the range `[1..50,000]`;
- each element of arrays `A` and `B` is an integer within the range `[0..N]`;
- the distance from guard post 0 to any other post is not greater than `900` bridges.

Write an **efficient** algorithm.

## Files

| File | Purpose |
|------|---------|
| `README.md` | This description. |
| `requirements.txt` | Dependencies of this mini-project. |
| `tree_product.ipynb` | Sizes + nested/unrelated cuts solution, two references and timing. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_2_2016_contest/04_tree_product/requirements.txt
jupyter lab codility/exercise_2_2016_contest/04_tree_product/tree_product.ipynb
```

## Hints

1. Root the tree at post 0 and compute the subtree size `s[v]` of every node: cutting the bridge above `v` separates `s[v]` posts.
2. With two cuts (above `a` and above `b`) there are two shapes: **nested** (`a` below `b`: sizes `s[a]`, `s[b] - s[a]`, `T - s[b]`) and **unrelated** (sizes `s[a]`, `s[b]`, `T - s[a] - s[b]`), with `T = N + 1`. Also consider one cut and no cut.
3. Nested pairs: for every node walk up its ancestors. The depth is at most 900, so this is O(N * depth); NumPy makes it fast.
4. Unrelated pairs: for a fixed `a`, `s[b] * (T - s[a] - s[b])` is concave in `s[b]`, so only the closest sizes below and above `(T - s[a]) / 2` matter. Keep a sorted list of the sizes of the nodes already **finished** by a DFS when `a` is entered: they are exactly the nodes unrelated to `a` that come earlier.
5. Return the result as a string. Compare with a brute force that tries every pair of bridges.
