import pytest
from pages.login_page import LoginPage
from pages.todo_page import TodoPage


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