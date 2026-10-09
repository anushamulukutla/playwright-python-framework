from playwright.async_api import Page, expect
from locators.locators import Locators


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.saucelabs_backpack = Locators.saucelabs_backpack
        self.shopping_cart = ".shopping_cart_link"
        self.saucelabs_bike_light = Locators.saucelabs_bike_light
        self.cart_button = Locators.cart_button



    async def add_sauce_labs_backpack_to_cart(self):
        await self.page.locator(self.saucelabs_backpack).click()

    async def open_cart(self):
        await self.page.locator(self.shopping_cart).click()

    async def add_sauce_labs_bike_light_to_cart(self):
        await self.page.locator(self.saucelabs_bike_light).click()
    async def open_product_cart(self):
        await self.page.locator(self.shopping_cart).click()
    async def checkout(self):
        await self.page.locator(Locators.check_out_button).click()
    async def fill_checkout_information(self, first_name, last_name, postal_code):
        await self.page.locator(Locators.first_name).fill(first_name)
        await self.page.locator(Locators.last_name).fill(last_name)
        await self.page.locator(Locators.postal_code).fill(postal_code)
        await self.page.locator(Locators.continue_button).click()
    async def finish_checkout(self):
        await self.page.locator(Locators.finish_button).click()

