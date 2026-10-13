# Project 04 - Eigen-digits: PCA, clustering and classifiers

Analyse the scikit-learn `digits` data set (8x8 images of handwritten digits): build a small collection class, compress the images with PCA, cluster them and compare classifiers.

**Skills:** OOP (sequence-like class, slicing, dunder methods), NumPy, scikit-learn pipelines (`StandardScaler`, `PCA`, `KMeans`, `SVC`, `KNeighborsClassifier`), cross-validation ideas, matplotlib.
**Notebooks to review first:** 05 (OOP), 06 (NumPy), 10 (scikit-learn).

## How to work

1. Open `eigendigits.py`; `load_collection` is provided. The rest is yours.
2. `python -m pytest projects/04_ml_eigendigits -q` (skipped = not implemented yet; the ML tests take a few seconds).

## Milestones

1. `Digit` and `Collection` - a read-only sequence of digits (`len`, indexing, slicing returns a `Collection`, `by_label`, `to_matrix`).
2. PCA - `fit_pca`, `components_for_variance`, `eigen_images`, `reconstruction_error`.
3. Unsupervised - `cluster_scores`, `cluster_purity`.
4. Supervised - `compare_classifiers`, `decision_grid` (2-D decision regions).

## Stretch goals

- Plot the mean digit and the first 16 eigen-images; reconstruct a digit with 2, 5, 10, 30 components.
- Replace `KMeans` by `GaussianMixture` or hierarchical clustering and compare the purity.
- Use `GridSearchCV` to tune `C` and `gamma` of the SVM (train/test split, no leakage!).
- Put scaler + PCA + classifier in a single `Pipeline` and save it with `joblib`.
