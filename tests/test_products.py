class TestProducts:
    def test_add_sauce_labs_backpack_to_cart(self, login):
        products_page = login

        products_page.add_sauce_labs_backpack_to_cart()

        assert products_page.page.get_by_role(
            "button", name="Remove"
        ).is_visible()

        products_page.open_cart()