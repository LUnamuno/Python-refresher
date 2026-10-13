# Projects

Six small, independent projects. Each folder has a starter module (`raise NotImplementedError` stubs with detailed docstrings), a test file that acts as the specification, and a `README.md` with milestones and stretch goals.

| # | Project | Main skills | Review notebooks |
|---|---------|-------------|------------------|
| 01 | `01_expense_tracker` | dataclasses, OOP, JSON, `argparse`, `datetime` | 02, 03, 05 |
| 02 | `02_dna_kmer_profiler` | strings, dicts, generators, NumPy, timing | 01, 04, 06, 11 |
| 03 | `03_data_analysis_pandas` | pandas cleaning, `groupby`, resample, rolling | 07, 08 |
| 04 | `04_ml_eigendigits` | sequence class, PCA, k-means, SVM/kNN | 05, 06, 10 |
| 05 | `05_signal_denoiser` | FFT, SciPy filters, metrics, 2-D FFT | 06, 07, 09 |
| 06 | `06_algorithm_toolkit` | algorithms, DP, graphs, LRU cache, complexity | 12-15, 04, 05 |

Suggested order: 01 -> 02 -> 06 (core Python), then 03 -> 05 -> 04 (scientific stack). Any order works.

## Workflow

```powershell
# from the repository root, with the virtual environment active
python -m pytest projects/01_expense_tracker -q     # one project
python -m pytest projects -q                        # all projects
python -m pytest projects -q -m "not slow"          # skip performance tests
```

- **Skipped** test = function not implemented yet (the skipped count is your progress bar).
- **Passed** = done. **Failed** = read the assertion message; the tests compare with examples, edge cases and brute-force solutions.
- Work on a git branch per project and commit often (notebook 16 reviews the git workflow).
- When a project passes, run `black`, `isort`, `flake8` and `mypy` on it (notebook 11) and refactor.
