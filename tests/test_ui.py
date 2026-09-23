from playwright.sync_api import expect
from pages.dynamic_loading_page import DynamicLoadingPage


def test_initial_state_before_loading(page):
    dynamic_page = DynamicLoadingPage(page)
    dynamic_page.navigate()

    expect(dynamic_page.start_button).to_be_visible()
    expect(dynamic_page.finish_text).not_to_be_visible()


def test_successful_dynamic_load(page):
    dynamic_page = DynamicLoadingPage(page)
    dynamic_page.navigate()
    dynamic_page.start_loading()

    expect(dynamic_page.loading_bar).not_to_be_visible(timeout=10000)
    expect(dynamic_page.finish_text).to_be_visible()
    expect(dynamic_page.finish_text).to_have_text("Hello World!")