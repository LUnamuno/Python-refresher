"""Project 04 - Eigen-digits: the Summer School "eigenfaces" session, redone on scikit-learn's digits dataset.

The original session defined a ``Diputado`` class, a ``Parlament`` container, computed a PCA of 7310-pixel faces, clustered
the scores with k-means and classified gender with a non-linear classifier. Here the "members" are 8x8 digit images.

Fill in every function / method marked ``raise NotImplementedError`` and run::

    python -m pytest projects/04_ml_eigendigits -q
"""
from __future__ import annotations
from collections.abc import Iterator
from dataclasses import dataclass
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
IMAGE_SHAPE = (8, 8)

@dataclass
class Digit:
    """One sample (the analogue of ``Diputado``): ``ind`` (identifier), ``label`` (0-9) and ``pixels``
    (flat array with 64 grey values). Property ``image`` returns the pixels reshaped to ``IMAGE_SHAPE``."""
    ind: int
    label: int
    pixels: np.ndarray

    @property
    def image(self) -> np.ndarray:
        raise NotImplementedError

class Collection:
    """Container of ``Digit`` objects (the analogue of ``Parlament``) that behaves like a read-only sequence."""

    def __init__(self, digits: list[Digit] | None=None) -> None:
        """Store a copy of the given list (default: empty)."""
        raise NotImplementedError

    @classmethod
    def from_arrays(cls, X: np.ndarray, y: np.ndarray) -> 'Collection':
        """Build one ``Digit`` per row: ``ind`` is the row number, ``label`` ``int(y[i])``, ``pixels`` the row."""
        raise NotImplementedError

    def add(self, digit: Digit) -> None:
        """Append a digit."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __getitem__(self, key):
        """``c[3]`` returns a ``Digit``; ``c[2:5]`` returns a new ``Collection`` (slices must keep the type)."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[Digit]:
        raise NotImplementedError

    def by_label(self, label: int) -> 'Collection':
        """A new ``Collection`` with only the digits having this label."""
        raise NotImplementedError

    def to_matrix(self) -> tuple[np.ndarray, np.ndarray]:
        """``(X, y)``: ``X`` has shape ``(n, 64)``, ``y`` shape ``(n,)`` (an empty collection gives ``(0, 64)`` and ``(0,)``)."""
        raise NotImplementedError

def load_collection() -> Collection:
    """PROVIDED. All 1797 digits of ``sklearn.datasets.load_digits`` as a ``Collection``."""
    data = load_digits()
    return Collection.from_arrays(data.data, data.target)

def fit_pca(X: np.ndarray, n_components: int) -> tuple[PCA, np.ndarray]:
    """Standardise ``X`` (zero mean, unit variance per column; constant columns must not produce NaN: use
    ``StandardScaler``), fit ``PCA(n_components, random_state=0)`` on it and return ``(pca, scores)`` where ``scores`` has
    shape ``(n_samples, n_components)``."""
    raise NotImplementedError

def components_for_variance(X: np.ndarray, target: float=0.9) -> int:
    """Smallest number of principal components (of the standardised data) that explains at least ``target`` of the variance
    (``0 < target <= 1``). Hint: fit a full PCA and use ``np.cumsum(explained_variance_ratio_)``."""
    raise NotImplementedError

def eigen_images(pca: PCA) -> np.ndarray:
    """The principal axes as images: array of shape ``(n_components, 8, 8)`` (the "eigen-digits")."""
    raise NotImplementedError

def reconstruction_error(X: np.ndarray, n_components: int) -> float:
    """Mean squared error between the standardised data and its reconstruction from ``n_components`` components
    (``inverse_transform`` of the scores). It must decrease as ``n_components`` grows; with all components it is ~0."""
    raise NotImplementedError

def cluster_scores(scores: np.ndarray, k: int, seed: int=0) -> np.ndarray:
    """k-means labels (``KMeans(n_clusters=k, n_init=10, random_state=seed)``) of the PCA scores."""
    raise NotImplementedError

def cluster_purity(clusters: np.ndarray, y: np.ndarray) -> float:
    """Purity of a clustering: for each cluster count its most frequent true label, sum these counts and divide by the
    number of samples. 1.0 = every cluster contains a single digit."""
    raise NotImplementedError

def compare_classifiers(X: np.ndarray, y: np.ndarray, n_components: int=20, cv: int=5) -> dict[str, float]:
    """Mean ``cv``-fold cross-validated accuracy of ``{"knn": ..., "svc": ...}``. Both are pipelines
    ``StandardScaler -> PCA(n_components) -> classifier`` (so nothing leaks from the validation folds):
    ``KNeighborsClassifier(5)`` and ``SVC(kernel="rbf", C=10, gamma="scale")``."""
    raise NotImplementedError

def decision_grid(model, X2: np.ndarray, step: float=0.1) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Decision regions of an already *fitted* 2-D classifier: return ``(xx, yy, zz)`` where ``xx, yy = np.meshgrid(...)``
    cover the bounding box of ``X2`` plus a margin of 1 unit in every direction (grid spacing ``step``) and ``zz`` holds
    ``model.predict`` for every grid point (same shape as ``xx``). Ready for ``plt.contourf(xx, yy, zz)``."""
    raise NotImplementedError
