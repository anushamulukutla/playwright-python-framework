import pytest
import test_data.products as products
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import time

@pytest.mark.asyncio
class TestProducts:

    async def test_add_sauce_labs_backpack_to_cart(self, login):
        products_page = login

        await products_page.add_sauce_labs_backpack_to_cart()

        assert await products_page.page.get_by_role(
            "button", name="Remove"
        ).is_visible()

        await products_page.open_cart()

    async def test_add_sauce_labs_bike_light_to_cart(self, login):
        products_page = login
        await products_page.add_sauce_labs_bike_light_to_cart()
        await products_page.open_product_cart()
        await products_page.page.get_by_role("button", name="Remove").is_visible()
        await products_page.checkout()
        await products_page.fill_checkout_information(products.FIRSTNAME, products.LASTNAME, products.POSTALCODE)
        await products_page.finish_checkout()

        await products_page.page.get_by_text("THANK YOU FOR YOUR ORDER").is_visible()
        #screenshot
        await products_page.page.screenshot(path="screenshots/checkout_complete.png")
        time.sleep(4)

