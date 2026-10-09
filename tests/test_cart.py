import pytest
from pages.cart_page import CartPage


@pytest.mark.asyncio
class TestCart:

    async def test_backpack_is_displayed_in_cart(self, login):
        products_page = login

        # Add Backpack to cart
        await products_page.add_sauce_labs_backpack_to_cart()

        # Open cart
        await products_page.open_cart()

        # Verify Backpack is displayed in cart
        cart_page = CartPage(products_page.page)
        await cart_page.verify_backpack_in_cart()
