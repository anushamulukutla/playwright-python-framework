from playwright.async_api import Page, expect
from locators.locators import Locators


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = Locators.username
        self.password = Locators.password
        self.login_button = Locators.login_button

    async def login(self, username, password):
        await self.page.fill(
            f'input[name="{self.username}"]',
            username
        )

        await self.page.fill(
            f'input[name="{self.password}"]',
            password
        )

        await self.page.click(
            f'#{self.login_button}'
        )
# from playwright.sync_api import Page
# from locators.locators import Locators


# class LoginPage:

#     def __init__(self, page: Page):

#         self.page = page

#         self.username = Locators.username
#         self.password = Locators.password
#         self.login_button = Locators.login_button

#     def login(self, username, password):
#         self.page.fill(f'input[name="{self.username}"]', username)
#         self.page.fill(f'input[name="{self.password}"]', password)
#         self.page.click(f'#{self.login_button}')