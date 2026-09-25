import pytest

from pages.dynamic_loading_page import DynamicLoadingPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    lp = LoginPage(page)
    lp.navigate()
    return lp


@pytest.fixture
def dynamic_page(page):
    dp = DynamicLoadingPage(page)
    dp.navigate()
    return dp