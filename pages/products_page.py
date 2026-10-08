from playwright.async_api import Page, expect
from locators.locators import Locators


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.saucelabs_backpack = Locators.saucelabs_backpack
        self.shopping_cart = ".shopping_cart_link"

    async def add_sauce_labs_backpack_to_cart(self):
        await self.page.locator(self.saucelabs_backpack).click()

    async def open_cart(self):
        await self.page.locator(self.shopping_cart).click()