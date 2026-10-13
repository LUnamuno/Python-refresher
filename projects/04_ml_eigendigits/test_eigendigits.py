import numpy as np
import pytest
from sklearn.neighbors import KNeighborsClassifier

from eigendigits import (
    Collection,
    Digit,
    cluster_purity,
    cluster_scores,
    compare_classifiers,
    components_for_variance,
    decision_grid,
    eigen_images,
    fit_pca,
    load_collection,
    reconstruction_error,
)


@pytest.fixture(scope="module")
def data():
    return load_collection().to_matrix()


# ---------------------------------------------------------------------------------------------------- Digit / Collection
def test_digit_image_property():
    d = Digit(7, 3, np.arange(64.0))
    assert d.image.shape == (8, 8) and d.image[1, 0] == 8


def test_collection_basics():
    X, y = np.arange(12.0).reshape(3, 4), np.array([5, 6, 5])
    # tiny arrays are fine for the container: it does not care about the pixel count
    c = Collection.from_arrays(X, y)
    assert len(c) == 3 and c[0].ind == 0 and c[2].label == 5 and list(c[1].pixels) == [4, 5, 6, 7]
    assert [d.ind for d in c] == [0, 1, 2]


def test_collection_slice_returns_collection():
    c = Collection.from_arrays(np.zeros((5, 4)), np.arange(5))
    part = c[1:4]
    assert isinstance(part, Collection) and len(part) == 3 and part[0].ind == 1
    assert isinstance(c[-1], Digit) and c[-1].ind == 4


def test_collection_add_and_filter():
    c = Collection()
    assert len(c) == 0
    for i, label in enumerate([1, 2, 1, 3]):
        c.add(Digit(i, label, np.zeros(64)))
    ones = c.by_label(1)
    assert isinstance(ones, Collection) and [d.ind for d in ones] == [0, 2]
    assert len(c.by_label(9)) == 0


def test_collection_copies_input_list():
    items = [Digit(0, 0, np.zeros(64))]
    c = Collection(items)
    items.append(Digit(1, 1, np.zeros(64)))
    assert len(c) == 1


def test_to_matrix_roundtrip(data):
    X, y = data
    assert X.shape == (1797, 64) and y.shape == (1797,)
    X2, y2 = Collection.from_arrays(X, y).by_label(4).to_matrix()
    assert X2.shape[1] == 64 and set(y2) == {4} and len(y2) == (y == 4).sum()
    empty = Collection().to_matrix()
    assert empty[0].shape == (0, 64) and empty[1].shape == (0,)


# ---------------------------------------------------------------------------------------------------- PCA
def test_fit_pca_shapes_and_variance(data):
    X, _ = data
    pca, scores = fit_pca(X, 10)
    assert scores.shape == (1797, 10)
    assert np.all(np.isfinite(scores))
    ratios = pca.explained_variance_ratio_
    assert np.all(np.diff(ratios) <= 1e-12) and 0.3 < ratios.sum() < 0.8
    assert np.allclose(scores.mean(axis=0), 0, atol=1e-8)


def test_components_for_variance(data):
    X, _ = data
    n90 = components_for_variance(X, 0.9)
    n95 = components_for_variance(X, 0.95)
    assert 20 < n90 < n95 < 64
    assert components_for_variance(X, 1.0) <= 64
    pca, _ = fit_pca(X, n90)
    assert pca.explained_variance_ratio_.sum() >= 0.9
    pca, _ = fit_pca(X, n90 - 1)
    assert pca.explained_variance_ratio_.sum() < 0.9


def test_eigen_images(data):
    X, _ = data
    pca, _ = fit_pca(X, 5)
    images = eigen_images(pca)
    assert images.shape == (5, 8, 8)
    assert np.allclose(np.linalg.norm(images.reshape(5, -1), axis=1), 1.0)


def test_reconstruction_error_decreases(data):
    X, _ = data
    errors = [reconstruction_error(X, k) for k in (2, 10, 30, 60)]
    assert errors == sorted(errors, reverse=True)
    assert errors[-1] < 0.05 * errors[0]


# ---------------------------------------------------------------------------------------------------- clustering and classifiers
def test_clustering_purity(data):
    X, y = data
    _, scores = fit_pca(X, 20)
    labels = cluster_scores(scores, 10)
    assert labels.shape == y.shape and len(np.unique(labels)) == 10
    assert 0.55 < cluster_purity(labels, y) <= 1.0
    assert np.array_equal(labels, cluster_scores(scores, 10))                 # reproducible


def test_cluster_purity_extremes():
    y = np.array([0, 0, 1, 1, 2, 2])
    assert cluster_purity(np.array([0, 0, 1, 1, 2, 2]), y) == 1.0
    assert cluster_purity(np.zeros(6, dtype=int), y) == pytest.approx(2 / 6)


def test_compare_classifiers(data):
    X, y = data
    scores = compare_classifiers(X, y, n_components=20, cv=5)
    assert set(scores) == {"knn", "svc"}
    assert scores["svc"] > 0.93 and scores["knn"] > 0.88
    assert scores["svc"] >= scores["knn"]


def test_decision_grid(data):
    X, y = data
    _, scores = fit_pca(X, 2)
    model = KNeighborsClassifier(5).fit(scores, y)
    xx, yy, zz = decision_grid(model, scores, step=0.5)
    assert xx.shape == yy.shape == zz.shape
    assert xx.min() <= scores[:, 0].min() - 0.9 and xx.max() >= scores[:, 0].max() - 0.5
    assert yy.min() <= scores[:, 1].min() - 0.9
    assert set(np.unique(zz)) <= set(range(10)) and len(np.unique(zz)) > 3
