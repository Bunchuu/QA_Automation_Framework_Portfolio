class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.saucedemo.com/"
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')
        self.inventory_title = page.locator(".title")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()