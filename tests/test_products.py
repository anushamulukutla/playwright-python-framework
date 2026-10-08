import pytest


@pytest.mark.asyncio
class TestProducts:

    async def test_add_sauce_labs_backpack_to_cart(self, login):
        products_page = login

        await products_page.add_sauce_labs_backpack_to_cart()

        assert await products_page.page.get_by_role(
            "button", name="Remove"
        ).is_visible()

        await products_page.open_cart()
