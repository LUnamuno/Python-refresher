"""Repository-wide pytest configuration.

Practice stubs raise ``NotImplementedError``. Instead of showing a wall of red failures for work you have not done yet,
those tests are reported as **skipped** ("TODO"), so the summary line is a progress bar::

    python -m pytest codility projects -q        # 37 passed, 112 skipped
"""
import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        report.outcome = "skipped"
        path, line, _ = item.reportinfo()
        report.longrepr = (str(path), (line or 0) + 1, "TODO: not implemented yet")
