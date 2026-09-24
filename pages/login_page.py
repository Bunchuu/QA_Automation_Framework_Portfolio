class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/login"
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("button[type=submit]")
        self.flash_banner = page.locator("#flash")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()