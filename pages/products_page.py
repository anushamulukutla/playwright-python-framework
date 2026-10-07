from playwright.sync_api import Page
from locators.locators_login import Login_locators


class ProductsPage:
    #A special method that is automatically called when an object of the class is created.
    # It initializes the page and the locator for the "Sauce Labs Bike Light" product.

    def __init__(self, page: Page):
        #instance variable that holds the reference to the page object,
        # allowing interaction with the web page.
        self.page = page
        self.saucelabs_bike_light = Login_locators.saucelabs_bike_light
        self.add_to_cart_button = Login_locators.cart_icon
        self.checkout_button = Login_locators.checkout_button
        self.checkout_first_name = Login_locators.checkout_first_name
        self.checkout_last_name = Login_locators.checkout_last_name
        self.checkout_postal_code = Login_locators.checkout_postal_code
        self.continue_button = Login_locators.continue_button
        self.finish_button = Login_locators.finsh_button


    def add_sauce_labs_bike_light_to_cart(self):
        self.page.locator(self.saucelabs_bike_light).click()

    def go_to_cart(self):
        self.page.locator(self.add_to_cart_button).click()
    def go_to_checkout(self):
        self.page.locator(self.checkout_button).click()
    def fill_checkout_information(self, first_name, last_name, postal_code):
        self.page.fill(self.checkout_first_name, first_name)
        self.page.fill(self.checkout_last_name, last_name)
        self.page.fill(self.checkout_postal_code, postal_code)
    def click_continue(self):
        self.page.locator(self.continue_button).click()

    def click_finish(self):
        self.page.locator(self.finish_button).click()



