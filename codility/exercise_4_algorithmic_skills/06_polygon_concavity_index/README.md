# 06 - PolygonConcavityIndex

**Codility:** [PolygonConcavityIndex](https://app.codility.com/programmers/trainings/4/polygon_concavity_index/) - Exercise 4, Algorithmic skills

Given a polygon, find a vertex that is not on the border of its convex hull (or report that the polygon is convex).

## Task description

An array `A` of points in a 2D plane is given. These points represent a polygon: every two consecutive points describe an edge of the polygon, and there is an edge connecting the last point and the first point in the array.

A set of points in a 2D plane, whose boundary is a straight line, is called a *semiplane*. More precisely, any set of the form `{(x, y) : ax + by >= c}` is a semiplane. The semiplane contains its boundary.

A polygon is *convex* if and only if no line segment between two points on the boundary ever goes outside the polygon. For example, the polygon whose vertices are consecutively `(-1, 3)`, `(3, 1)`, `(0, -1)`, `(-2, 1)` is convex.

The *convex hull* of a finite set of points in a 2D plane is the smallest convex polygon that contains all points in this set. For example, the convex hull of the seven points `(-1, 3)`, `(1, 2)`, `(3, 1)`, `(1, 1)`, `(0, -1)`, `(-2, 1)`, `(-1, 2)` is a polygon that has five vertices. When traversed clockwise, its vertices are `(-1, 3)`, `(1, 2)`, `(3, 1)`, `(0, -1)`, `(-2, 1)`.

If a polygon is concave (that is, it is not convex), it has a vertex which does not lie on its convex hull border. Your assignment is to find such a vertex.

Assume that the following declaration is given:

```python
from dataclasses import dataclass, field

@dataclass
class Point2D:
    x: int
    y: int
```

Write a function:

```python
def solution(A)
```

that, given a non-empty array `A` consisting of `N` elements describing a polygon, returns `-1` if the polygon is convex. Otherwise, the function should return the index of **any** point that doesn't belong to the convex hull border. Note that consecutive edges of the polygon may be collinear (that is, the polygon might have 180-degree angles).

To access the coordinates of the `K`-th point (`0 <= K < N`) use `A[K].x` and `A[K].y`.

For example, given points

```
A[0] = (-1,  3)
A[1] = ( 1,  2)
A[2] = ( 3,  1)
A[3] = ( 0, -1)
A[4] = (-2,  1)
```

the function should return `-1`, as explained above.

However, given points

```
A[0] = (-1,  3)
A[1] = ( 1,  2)
A[2] = ( 1,  1)
A[3] = ( 3,  1)
A[4] = ( 0, -1)
A[5] = (-2,  1)
A[6] = (-1,  2)
```

the function should return either `2` or `6`. These are the indices of the points lying strictly inside the convex hull (that is, not on the convex hull border).

### Assumptions

- `N` is an integer within the range `[3..10,000]`;
- the coordinates of each point in array `A` are integers within the range `[-1,000,000,000..1,000,000,000]`;
- no two edges of the polygon `A` intersect, other than meeting at their endpoints;
- array `A` does not contain duplicate points.

Write an **efficient** algorithm.

## Files

| File                                | Purpose                                                                 |
|-------------------------------------|-------------------------------------------------------------------------|
| `README.md`                         | This description.                                                       |
| `requirements.txt`                  | Dependencies of this mini-project.                                      |
| `polygon_concavity_index.ipynb`     | Convex hull solution, independent geometric reference and random polygons. |

## How to work

```powershell
# from the repository root
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r codility/exercise_4_algorithmic_skills/06_polygon_concavity_index/requirements.txt
jupyter lab codility/exercise_4_algorithmic_skills/06_polygon_concavity_index/polygon_concavity_index.ipynb
```

## Hints

1. The polygon is concave exactly when some vertex is **strictly inside** the convex hull of the points. So: compute the convex hull of all vertices, and return any vertex that is not on its border.
2. Use **Andrew's monotone chain** algorithm: sort the points by `(x, y)`, build the lower chain and the upper chain with the cross product (`cross(o, a, b) = (a.x-o.x)*(b.y-o.y) - (a.y-o.y)*(b.x-o.x)`).
3. Collinear points on the hull border count as border points, so pop only on a **strictly** right turn (`cross < 0`). The chains then keep the collinear points.
4. Work with indices, not with points, so the answer is directly the index to return.
5. Coordinates go up to `10^9`; the cross product reaches about `8 * 10^18`. Python integers are unbounded, but in C++/Java use 64-bit with care.
6. Complexity: O(N log N) time (the sort), O(N) space.
