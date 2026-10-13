# 03 - SparseBinaryDecomposition

**Codility:** [SparseBinaryDecomposition](https://app.codility.com/programmers/trainings/9/sparse_binary_decomposition/) - Exercise 9, Bitwise operations - *hard*

Decompose an integer into a sum of two integers having no consecutive 1s in binary form.

## Task description

A non-negative integer `N` is called *sparse* if its binary representation does not contain two consecutive bits set to 1. For example, `41` is sparse, because its binary representation is `101001` and it does not contain two consecutive 1s. On the other hand, `26` is not sparse, because its binary representation is `11010` and it contains two consecutive 1s.

Two non-negative integers `P` and `Q` are called a *sparse decomposition* of integer `N` if `P` and `Q` are sparse and `N = P + Q`.

For example:

- `8` and `18` are a sparse decomposition of `26` (`1000` and `10010`).
- `9` and `17` are a sparse decomposition of `26` (`1001` and `10001`).
- `2` and `24` are **not** a sparse decomposition of `26`; though `2 + 24 = 26`, the binary representation of `24` is `11000`, which is not sparse.

Write a function:

```python
def solution(N)
```

that, given a non-negative integer `N`, returns any integer that is one part of a sparse decomposition of `N`. The function should return `-1` if there is no sparse decomposition of `N`.

For example, given `N = 26` the function may return `8`, `9`, `17` or `18`, as explained above. All other possible results for `N = 26` are `5`, `10`, `16` and `21`.

### Assumptions

- `N` is an integer within the range `[0..1,000,000,000]`.

Write an **efficient** algorithm.

## Files

| File                                | Purpose                                                              |
|-------------------------------------|----------------------------------------------------------------------|
| `README.md`                         | This description.                                                    |
| `requirements.txt`                  | Dependencies of this mini-project.                                   |
| `sparse_binary_decomposition.ipynb` | Solution (digit DP), official example, validator and brute-force check. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_9_bit_ops/03_sparse_binary_decomposition/requirements.txt
jupyter lab codility/exercise_9_bit_ops/03_sparse_binary_decomposition/sparse_binary_decomposition.ipynb
```

## Hints

1. The answer is not unique, so test it with a **validator** (`is_sparse(P)`, `is_sparse(N - P)`, `0 <= P <= N`) instead of comparing with one fixed value.
2. A brute force over all `P <= N` is O(N): fine for tiny `N` (use it as a reference), impossible for `N = 10**9`.
3. Think of adding `P + Q` in binary, bit by bit from the least significant one. At each bit you choose `p_i` and `q_i`; the sum bit `(p_i + q_i + carry) % 2` must equal bit `i` of `N`, and the new carry is `(p_i + q_i + carry) // 2`.
4. The only memory you need: the previous bit of `P`, the previous bit of `Q` and the carry. That is a **digit DP** with 8 states per position and about 32 positions.
5. Reconstruct `P` while unwinding the recursion (or store the choices). If the start state cannot reach "carry 0 after the last bit", return `-1`.
6. Complexity: O(log N) time and space.
