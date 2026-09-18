from playwright.sync_api import Page
from locators.locators_login import Login_locators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = Login_locators.username
        self.password = Login_locators.password
        self.login_button = Login_locators.login_button

    def login(self, username, password):
        self.page.fill(f'input[name="{self.username}"]', username)
        self.page.fill(f'input[name="{self.password}"]', password)
        self.page.click(f'#{self.login_button}')