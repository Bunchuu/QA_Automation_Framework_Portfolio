class DynamicLoadingPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/dynamic_loading/1"
        self.start_button = page.locator("#start button")
        self.loading_bar = page.locator("#loading")
        self.finish_text = page.locator("#finish h4")

    def navigate(self):
        self.page.goto(self.url)

    def start_loading(self):
        self.start_button.click()