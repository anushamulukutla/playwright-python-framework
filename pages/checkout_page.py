class CheckoutPage:

    def __init__(self, page):
        self.page = page

        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

    async def fill_checkout_information(
        self, first_name, last_name, postal_code
    ):
        await self.first_name_input.fill(first_name)
        await self.last_name_input.fill(last_name)
        await self.postal_code_input.fill(postal_code)

    async def click_continue(self):
        await self.continue_button.click()

    async def click_finish(self):
        await self.finish_button.click()