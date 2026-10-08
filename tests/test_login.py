import pytest
from playwright.async_api import Page, expect
from pages.login_page import LoginPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD
from utils.screenshots import screenshot


@pytest.mark.asyncio
class TestLogin:

    async def test_login(self, page):
        login_page = LoginPage(page)

        await page.goto(BASE_URL)
        await login_page.login(STANDARD_USER, STANDARD_PASSWORD)

        assert page.url == f"{BASE_URL}/inventory.html"

    async def test_login_with_locked_out_user(self, page):
        login_page = LoginPage(page)

        await page.goto(BASE_URL)
        await login_page.login("locked_out_user", "secret_sauce")

        error = page.locator("[data-test='error']")
        await expect(error).to_be_visible()
        await expect(error).to_contain_text(
            "Sorry, this user has been locked out"
        )

        await screenshot.take_screenshot(page, "locked_out_user_error")

    async def test_login_with_problem_user(self, page):
        login_page = LoginPage(page)

        await page.goto(BASE_URL)
        await login_page.login("problem_user", "secret_sauce")

        assert page.url == f"{BASE_URL}/inventory.html"

        await screenshot.take_screenshot(page, "locked_out_user_error")