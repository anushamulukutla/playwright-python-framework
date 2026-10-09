import pytest
import test_data.products as products

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.asyncio
class TestCheckout:

    async def test_backpack_checkout(self, login):
        products_page = login

        # Step 1: Add Backpack to cart
        await products_page.add_sauce_labs_backpack_to_cart()

        # Step 2: Open cart
        await products_page.open_cart()

        # Step 3: Click Checkout
        cart_page = CartPage(products_page.page)
        await cart_page.click_checkout()

        # Step 4: Fill checkout information
        checkout_page = CheckoutPage(products_page.page)

        await checkout_page.fill_checkout_information(
            products.FIRSTNAME,
            products.LASTNAME,
            products.POSTALCODE
        )

        # Step 5: Click Continue
        await checkout_page.click_continue()

        # Step 6: Verify Checkout Overview page
        # assert await products_page.page.get_by_text(
        #     "Checkout: Overview"
        # ).is_visible()
        await products_page.page.get_by_text("Checkout: Overview").wait_for(state="visible")

        # Step 7: Finish checkout
        await checkout_page.click_finish()

        # Step 8: Verify successful order
        assert await products_page.page.get_by_text(
            "THANK YOU FOR YOUR ORDER"
        ).is_visible()
