import pytest
from pages.login_page import LoginPage
from pages.dynamic_loading_page import DynamicLoadingPage


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