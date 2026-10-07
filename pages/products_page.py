from playwright.sync_api import Page
from locators.locators import Locators
class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.saucelabs_backpack = Locators.saucelabs_backpack
        self.shopping_cart = ".shopping_cart_link"

    def add_sauce_labs_backpack_to_cart(self):
        self.page.locator(self.saucelabs_backpack).click()

    def open_cart(self):
        self.page.locator(self.shopping_cart).click()