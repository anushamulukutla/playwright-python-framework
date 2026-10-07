import time
import pytest
from playwright.sync_api import expect

from pages import login_page
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD, FIRSTNAME, LASTNAME, POSTALCODE
from utils.screenshots import screenshot
from playwright.sync_api import expect

class TestProducts():

    def test_add_product(self, logged_in_page):
        products_page = ProductsPage(logged_in_page)

        logged_in_page.goto(BASE_URL + "/inventory.html")
        products_page.add_sauce_labs_bike_light_to_cart()
        #click on the cart icon to go to the cart page
        products_page.go_to_cart()
        products_page.go_to_checkout()
        products_page.fill_checkout_information(FIRSTNAME, LASTNAME, POSTALCODE)
        products_page.click_continue()
        expect(logged_in_page.locator('[data-test="secondary-header"]')).to_have_text("Checkout: Overview")
        products_page.click_finish()
        print("\nProduct added to cart and checkout information filled successfully.")

        time.sleep(5)





        # Verify that the product was added to the cart



    #login -> click on add prdouct

