from playwright.sync_api import expect


def test_initial_state_before_loading(dynamic_page):

    expect(dynamic_page.start_button).to_be_visible()
    expect(dynamic_page.finish_text).not_to_be_visible()


def test_successful_dynamic_load(dynamic_page):
    dynamic_page.start_loading()

    expect(dynamic_page.loading_bar).not_to_be_visible(timeout=10000)
    expect(dynamic_page.finish_text).to_be_visible()
    expect(dynamic_page.finish_text).to_have_text("Hello World!")


def test_successful_login(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")

    expect(login_page.flash_banner).to_contain_text("You logged into a secure area!")


def test_failed_login_shows_error(login_page):
    login_page.login("wrong_username", "WrongPassword!")

    expect(login_page.flash_banner).to_contain_text("Your username is invalid!")