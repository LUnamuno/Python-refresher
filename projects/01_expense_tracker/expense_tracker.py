"""Project 01 - Expense tracker: a small command-line tool that keeps expenses in a JSON file.

Fill in every function / method marked ``raise NotImplementedError`` and run::

    python -m pytest projects/01_expense_tracker -q

Try the finished tool with::

    python projects/01_expense_tracker/expense_tracker.py add 12.5 food --note "lunch"
    python projects/01_expense_tracker/expense_tracker.py list
    python projects/01_expense_tracker/expense_tracker.py report
"""
from __future__ import annotations
import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
DEFAULT_FILE = 'expenses.json'

@dataclass(frozen=True)
class Expense:
    """One expense (immutable).

    * ``amount`` must be > 0, otherwise raise ``ValueError``.
    * ``category`` is normalised to lower case without surrounding blanks; an empty category raises ``ValueError``.
      (Frozen dataclasses cannot assign attributes in ``__post_init__``: use ``object.__setattr__``.)
    """
    day: date
    amount: float
    category: str
    note: str = ''

    def __post_init__(self) -> None:
        raise NotImplementedError

    def to_dict(self) -> dict:
        """JSON-friendly dict: ``{"day": "2024-03-05", "amount": 12.5, "category": "food", "note": ""}``."""
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict) -> 'Expense':
        """Inverse of ``to_dict`` (``day`` is an ISO string; ``note`` may be missing)."""
        raise NotImplementedError

class ExpenseStore:
    """A list of expenses persisted in a JSON file (a list of ``Expense.to_dict()`` items)."""

    def __init__(self, path: str | Path) -> None:
        """Remember ``path``; if the file exists load its content, otherwise start empty (do not create the file yet)."""
        raise NotImplementedError

    def _load(self) -> None:
        """Read ``self.path`` and fill ``self._items``."""
        raise NotImplementedError

    def save(self) -> None:
        """Write all expenses to ``self.path`` as pretty-printed JSON (``indent=2``); create parent folders if needed."""
        raise NotImplementedError

    def add(self, expense: Expense) -> None:
        """Append ``expense`` and save immediately."""
        raise NotImplementedError

    def all(self) -> list[Expense]:
        """All expenses sorted by day (stable: same-day expenses keep insertion order). Return a new list."""
        raise NotImplementedError

    def remove(self, index: int) -> Expense:
        """Remove and return the expense at position ``index`` of ``all()``; save. ``IndexError`` if out of range."""
        raise NotImplementedError

    def between(self, start: date, end: date) -> list[Expense]:
        """Expenses with ``start <= day <= end`` (both inclusive), sorted by day."""
        raise NotImplementedError

    def total(self, category: str | None=None) -> float:
        """Sum of all amounts, or only of ``category`` (case-insensitive) when given. Empty -> 0.0."""
        raise NotImplementedError

    def by_category(self) -> dict[str, float]:
        """``{category: total}`` ordered by total, biggest first (ties: alphabetical)."""
        raise NotImplementedError

    def monthly_totals(self) -> dict[str, float]:
        """``{"YYYY-MM": total}`` ordered chronologically."""
        raise NotImplementedError

def build_parser() -> argparse.ArgumentParser:
    """Create the CLI parser.

    ``--file PATH`` (default ``expenses.json``) before the sub-command, then one of:

    * ``add AMOUNT CATEGORY [--note TEXT] [--date YYYY-MM-DD]``  (date defaults to today)
    * ``list [--category NAME]``
    * ``report``
    * ``remove INDEX`` (position as shown by ``list``, starting at 1)

    Store the chosen sub-command in ``args.command``.
    """
    raise NotImplementedError

def main(argv: list[str] | None=None) -> int:
    """Run the CLI and return the exit code (0 = ok, 2 = user error, message on ``sys.stderr``).

    Output contract (tests check these substrings):

    * ``add``   -> ``Added: 2024-03-05 12.50 food``
    * ``list``  -> one line per expense, numbered from 1: ``1  2024-03-05    12.50  food  lunch``;
      ``No expenses.`` when there is nothing to show.
    * ``report``-> ``Total: 42.00`` then a ``By category:`` block (``  food: 30.00``) and a ``By month:`` block
      (``  2024-03: 42.00``).
    * ``remove``-> ``Removed: 2024-03-05 12.50 food``; an invalid index prints ``error: ...`` and returns 2.
    * invalid amount / category in ``add`` -> ``error: <message>`` on stderr, return 2.
    """
    raise NotImplementedError
if __name__ == '__main__':
    raise SystemExit(main())
