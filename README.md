# Python Refresher

A self-study repository to refresh Python, built from three sources:

1. **Python Summer School** slides (`CursP_BasePython`, `CursP_Numpy_Matplotlib`, `CursP_sklearn`, `BonusSlides`).
2. **Python Bootcamp** (BP1-BP9: setup, language, decorators/iterators/typing, OOP, scientific stack, code quality, testing, git, CI/CD/Docker).
3. **Codility lessons** (17 lessons on algorithms and complexity).

The material is organised in three layers:

| Folder | What it is | How to use it |
|--------|------------|---------------|
| `notebooks/` | Executed Jupyter notebooks that summarise the sources with runnable examples and exercises. | Read, run, change the code, do the "Your turn" cells. |
| `codility/` | Practice stubs (`practice_0X_*.py`) with tests (`test_practice_0X_*.py`) for the Codility tasks. | Implement the stubs until the tests pass. |
| `projects/` | Six small, independent projects (starter module + tests + README). | Build one after the matching notebooks. |

## Setup (Windows / PowerShell)

```powershell
cd C:\Users\leire\Projects\Python-Refresher
python -m venv .venv
.\.venv\Scripts\Activate.ps1          # if scripts are blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name python-refresher --display-name "Python (refresher)"
jupyter lab                            # or open the .ipynb files in Cursor / VS Code
```

In Cursor / VS Code install the **Jupyter** and **Python** extensions, open a notebook and choose the `.venv` interpreter as kernel.
The notebooks were run with Python 3.12, NumPy 2, pandas 3, SciPy 1.18 and scikit-learn 1.9.

## Study plan

| Phase | Notebooks | Then practise with |
|-------|-----------|--------------------|
| 1. Core language | 00, 01, 02, 03 | `projects/01_expense_tracker` |
| 2. Pythonic tools and OOP | 04, 05 | `projects/06_algorithm_toolkit` (data structure part) |
| 3. Scientific stack | 06, 07, 08, 09, 10 | projects 02, 03, 04, 05 |
| 4. Professional workflow | 11, 16 | add tests, linting, CI to any project |
| 5. Algorithms | 12, 13, 14, 15 | `codility/` practice files, `projects/06_algorithm_toolkit` |

Suggested rhythm: 4-5 notebooks per week, one project per notebook block, 3-4 Codility tasks per day at the end.

## Where each source went

| Source | Content | Notebook(s) |
|--------|---------|-------------|
| Bootcamp BP1 | Setup, tooling, virtual environments, Docker dev containers | 00 |
| Summer School BasePython, Bootcamp BP2 | Types, strings, collections, control flow, functions, modules, I/O, standard library | 01, 02, 03 |
| Bootcamp BP3 | Iterators, generators, decorators, typing | 04 |
| Bootcamp BP4 | OOP, ABCs, Protocols, dataclasses | 05 |
| Summer School Numpy/Matplotlib, Bootcamp BP5 | NumPy, Matplotlib | 06, 07 |
| Bootcamp BP5 | pandas, SciPy, SymPy | 08, 09 |
| Summer School sklearn | Supervised and unsupervised learning, PCA, model evaluation | 10 |
| BonusSlides, Bootcamp BP6-BP7 | Style, bandit, refactoring, profiling, unittest, pytest, mocking | 11 |
| Bootcamp BP8-BP9 | Git workflows, CI/CD (GitLab, GitHub Actions), Docker | 16 |
| Codility lessons 1-17 | Complexity, counting, prefix sums, sorting, stacks, leader, slices, primes, Euclid, search, greedy, DP | 12, 13, 14, 15 + `codility/` |

## Running the tests

```powershell
python -m pytest -q                     # codility + projects (see pytest.ini)
python -m pytest codility -q            # only the Codility practice
python -m pytest projects/03_data_analysis_pandas -q
python -m pytest -q -m "not slow"       # skip performance tests
```

An exercise whose function still raises `NotImplementedError` is reported as **skipped**, not failed. The number of skipped
tests is therefore your progress bar; a fresh checkout shows only skips (plus the few helpers that are provided).
A failing test means your implementation is wrong or too slow: read the assertion message.

## Rebuilding a notebook

The notebooks are saved with their outputs. To re-run one after editing:

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace notebooks\05_oop.ipynb
```

## Modernisation notes

The slides are from 2023 and the bootcamp is older; the notebooks use current versions and point out what changed:
pandas 3 (copy-on-write, `str` dtype), NumPy 2 (scalar types, removed aliases), scikit-learn (`load_boston` removed,
`sklearn.cross_validation` -> `sklearn.model_selection`), `venv` + `pip` instead of Docker-only environments, `pytest` next
to `unittest`, `pathlib` instead of `os.path`, f-strings and type hints everywhere.

## Progress checklist

- [ ] Phase 1: notebooks 00-03, project 01
- [ ] Phase 2: notebooks 04-05, project 06
- [ ] Phase 3: notebooks 06-10, projects 02-05
- [ ] Phase 4: notebooks 11 and 16, CI workflow added to this repo
- [ ] Phase 5: notebooks 12-15, all `codility/` practice tests passing
