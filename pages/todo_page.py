class TodoPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://demo.playwright.dev/todomvc/"
        self.todo_input = page.get_by_placeholder("What needs to be done?")
        self.todo_items = page.locator(".todo-list li")

    def navigate(self):
        self.page.goto(self.url)

    def add_todo(self, text):
        self.todo_input.fill(text)
        self.todo_input.press("Enter")