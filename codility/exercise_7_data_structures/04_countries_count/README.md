# 04 - CountriesCount

**Codility:** [CountriesCount](https://app.codility.com/programmers/trainings/7/countries_count/) - Exercise 7, Data Structures - *hard*

Count the number of different countries that a map contains.

## Task description

A rectangular map consisting of `N` rows and `M` columns of square areas is given. Each area is painted with a certain color.

Two areas on the map belong to the same country if the following conditions are met:

- they have the same color;
- it is possible to travel from one area to the other orthogonally (that is, by moving only north, south, west or east) without moving over areas of a different color.

The map can be described by a zero-indexed matrix `A` consisting of `N` rows and `M` columns of integers. The color of each area is described by the corresponding element of the matrix. Two areas have the same color if and only if their corresponding matrix elements have the same value.

For example, consider this matrix `A` with seven rows and three columns:

```
5 4 4
4 3 4
3 2 4
2 2 2
3 3 4
1 4 4
4 1 1
```

Matrix `A` describes a map colored with five colors. The areas belong to **eleven** different countries.

Write a function:

```python
def solution(A)
```

that, given a zero-indexed matrix `A` consisting of `N` rows and `M` columns of integers, returns the number of different countries to which the areas of the map described by matrix `A` belong.

For the matrix above the function should return `11`.

### Assumptions

- `N` and `M` are integers within the range `[1..300,000]`;
- the number of elements in matrix `A` is within the range `[1..300,000]`;
- each element of matrix `A` is an integer within the range `[-1,000,000,000..1,000,000,000]`.

Write an **efficient** algorithm.

## Files

| File                      | Purpose                                                                    |
|---------------------------|----------------------------------------------------------------------------|
| `README.md`               | This description.                                                          |
| `requirements.txt`        | Dependencies of this mini-project.                                         |
| `countries_count.ipynb`   | Flood-fill solution, union-find cross-check, edge cases and large inputs.  |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_7_data_structures/04_countries_count/requirements.txt
jupyter lab codility/exercise_7_data_structures/04_countries_count/countries_count.ipynb
```

## Hints

1. Countries are the **connected components** of the grid graph where two neighbouring cells are connected only if they have the same value.
2. Scan the cells in order; every time you find a cell not yet visited, you have found a new country: increment the counter and mark its whole component.
3. Marking the component can be done with BFS/DFS (use an explicit stack, **not** recursion: a single country can have 300,000 cells) or with union-find.
4. `N` or `M` can be 1 while the other is 300,000, so do not assume a square matrix. Store `visited` as a flat `bytearray` of size `N * M`.
5. Complexity: O(N * M) time and space.
