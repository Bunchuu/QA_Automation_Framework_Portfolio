import os

import pytest

from pages.login_page import LoginPage
from pages.todo_page import TodoPage


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def trace_on_failure(request):
    if "context" not in request.fixturenames:
        yield
        return

    context = request.getfixturevalue("context")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield
    call_rep = getattr(request.node, "rep_call", None)
    if call_rep and call_rep.failed:
        results_dir = "test-results"
        os.makedirs(results_dir, exist_ok=True)
        test_name = request.node.name.replace("[", "_").replace("]", "_").replace("/", "_")
        trace_path = os.path.join(results_dir, f"trace_{test_name}.zip")
        context.tracing.stop(path=trace_path)
    else:
        context.tracing.stop()


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def todo_page(page):
    tp = TodoPage(page)
    tp.navigate()
    return tp