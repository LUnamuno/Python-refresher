"""pytest configuration for the Codility practice files.

* A test whose function still ``raise NotImplementedError`` is reported as
  **skipped** (not failed), so you can solve the exercises one by one.
* Doctests in the ``practice_*.py`` stubs are handled the same way.
"""

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if (
        call.when == "call"
        and call.excinfo is not None
        and call.excinfo.errisinstance(NotImplementedError)
    ):
        report.outcome = "skipped"
        report.longrepr = (str(item.path), item.reportinfo()[1] or 0, "not implemented yet")
