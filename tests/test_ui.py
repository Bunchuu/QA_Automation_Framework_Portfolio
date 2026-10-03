import pytest
from playwright.sync_api import expect


def test_initial_state(todo_page):

    expect(todo_page.todo_input).to_be_visible()
    expect(todo_page.todo_items).to_have_count(0)


def test_add_todo_items(todo_page):
    todo_page.add_todo("Fly over the cuckoo's nest")
    expect(todo_page.todo_items).to_have_count(1)
    expect(todo_page.todo_items).to_have_text("Fly over the cuckoo's nest")

    todo_page.add_todo("Silence the lambs")
    expect(todo_page.todo_items).to_have_count(2)
    expect(todo_page.todo_items.last).to_contain_text("lambs")


def test_successful_login(login_page, page):
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.inventory_title).to_be_visible()
    expect(login_page.inventory_title).to_have_text("Products")


@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", 
     "Sorry, this user has been locked out."),
     ("standard_user", "wrong_password", 
      "Username and password do not match any user in this service"),
      ("", "secret_sauce", "Username is required")
])
def test_failed_login_shows_error(
    login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text(
        expected_error
        )