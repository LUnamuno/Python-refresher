import json
from datetime import date

import pytest

from expense_tracker import Expense, ExpenseStore, main


@pytest.fixture
def store(tmp_path):
    s = ExpenseStore(tmp_path / "db" / "expenses.json")
    s.add(Expense(date(2024, 3, 5), 12.5, "Food", "lunch"))
    s.add(Expense(date(2024, 2, 20), 30.0, "transport"))
    s.add(Expense(date(2024, 3, 1), 7.5, " food "))
    s.add(Expense(date(2024, 3, 31), 100.0, "rent"))
    return s


# ---------------------------------------------------------------------------------------------------- Expense
def test_expense_normalises_category():
    assert Expense(date(2024, 1, 1), 5, "  Food ").category == "food"


@pytest.mark.parametrize("amount, category", [(0, "food"), (-3, "food"), (5, ""), (5, "   ")])
def test_expense_validation(amount, category):
    with pytest.raises(ValueError):
        Expense(date(2024, 1, 1), amount, category)


def test_expense_is_immutable_and_comparable():
    e = Expense(date(2024, 1, 1), 5, "food")
    with pytest.raises(Exception):
        e.amount = 6                                    # frozen dataclass
    assert e == Expense(date(2024, 1, 1), 5, "FOOD")


def test_expense_dict_roundtrip():
    e = Expense(date(2024, 3, 5), 12.5, "food", "lunch")
    assert e.to_dict() == {"day": "2024-03-05", "amount": 12.5, "category": "food", "note": "lunch"}
    assert Expense.from_dict(e.to_dict()) == e
    assert Expense.from_dict({"day": "2024-03-05", "amount": 1, "category": "x"}).note == ""


# ---------------------------------------------------------------------------------------------------- ExpenseStore
def test_store_persists_to_disk(store, tmp_path):
    path = tmp_path / "db" / "expenses.json"
    assert path.exists()
    assert len(json.loads(path.read_text())) == 4
    reloaded = ExpenseStore(path)
    assert reloaded.all() == store.all()


def test_store_missing_file_starts_empty(tmp_path):
    s = ExpenseStore(tmp_path / "nothing.json")
    assert s.all() == [] and s.total() == 0.0
    assert not (tmp_path / "nothing.json").exists()


def test_all_is_sorted_and_a_copy(store):
    days = [e.day for e in store.all()]
    assert days == sorted(days)
    store.all().clear()
    assert len(store.all()) == 4


def test_between_is_inclusive(store):
    got = store.between(date(2024, 3, 1), date(2024, 3, 5))
    assert [e.amount for e in got] == [7.5, 12.5]
    assert store.between(date(2025, 1, 1), date(2025, 12, 31)) == []


def test_totals(store):
    assert store.total() == pytest.approx(150.0)
    assert store.total("food") == pytest.approx(20.0)
    assert store.total("FOOD") == pytest.approx(20.0)
    assert store.total("unknown") == 0.0


def test_by_category_is_sorted_by_total(store):
    result = store.by_category()
    assert list(result) == ["rent", "transport", "food"]
    assert result["food"] == pytest.approx(20.0)


def test_monthly_totals_chronological(store):
    assert store.monthly_totals() == {"2024-02": pytest.approx(30.0), "2024-03": pytest.approx(120.0)}
    assert list(store.monthly_totals()) == ["2024-02", "2024-03"]


def test_remove(store, tmp_path):
    removed = store.remove(0)                           # position in all(): the oldest, 2024-02-20
    assert removed.category == "transport"
    assert len(ExpenseStore(tmp_path / "db" / "expenses.json").all()) == 3
    with pytest.raises(IndexError):
        store.remove(10)
    with pytest.raises(IndexError):
        store.remove(-1)


# ---------------------------------------------------------------------------------------------------- CLI
def run(capsys, tmp_path, *args):
    code = main(["--file", str(tmp_path / "e.json"), *args])
    captured = capsys.readouterr()
    return code, captured.out, captured.err


def test_cli_add_list_report(capsys, tmp_path):
    assert run(capsys, tmp_path, "add", "12.5", "Food", "--note", "lunch", "--date", "2024-03-05")[0] == 0
    code, out, _ = run(capsys, tmp_path, "add", "30", "transport", "--date", "2024-02-20")
    assert code == 0 and "Added: 2024-02-20 30.00 transport" in out

    code, out, _ = run(capsys, tmp_path, "list")
    lines = out.strip().splitlines()
    assert code == 0 and len(lines) == 2
    assert lines[0].startswith("1") and "2024-02-20" in lines[0] and "transport" in lines[0]
    assert "lunch" in lines[1]

    _, out, _ = run(capsys, tmp_path, "list", "--category", "FOOD")
    assert "food" in out and "transport" not in out

    code, out, _ = run(capsys, tmp_path, "report")
    assert code == 0
    assert "Total: 42.50" in out and "food: 12.50" in out and "2024-03: 12.50" in out


def test_cli_empty_list(capsys, tmp_path):
    assert run(capsys, tmp_path, "list")[1].strip() == "No expenses."


def test_cli_errors_return_2(capsys, tmp_path):
    code, _, err = run(capsys, tmp_path, "add", "-5", "food")
    assert code == 2 and err.startswith("error:")
    code, _, err = run(capsys, tmp_path, "remove", "3")
    assert code == 2 and "error" in err


def test_cli_remove(capsys, tmp_path):
    run(capsys, tmp_path, "add", "10", "a", "--date", "2024-01-01")
    code, out, _ = run(capsys, tmp_path, "remove", "1")
    assert code == 0 and "Removed: 2024-01-01 10.00 a" in out
    assert run(capsys, tmp_path, "list")[1].strip() == "No expenses."
