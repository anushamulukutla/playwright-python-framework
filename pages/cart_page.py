class CartPage:

    def __init__(self, page):
        self.page = page

        self.backpack = page.get_by_text("Sauce Labs Backpack")
        self.checkout_button = page.get_by_role(
            "button", name="Checkout"
        )

    async def verify_backpack_in_cart(self):
        assert await self.backpack.is_visible()

    async def click_checkout(self):
        await self.checkout_button.click()
