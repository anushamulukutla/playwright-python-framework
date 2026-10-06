import time
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD
from utils.screenshots import screenshot
class TestLogin:
    def test_login(self, page):
        login_page = LoginPage(page)
        page.goto(BASE_URL)
        login_page.login(STANDARD_USER, STANDARD_PASSWORD)
        assert page.url == f"{BASE_URL}/inventory.html"

    def test_login_with_locked_out_user(self, page):
        login_page = LoginPage(page)
        page.goto(BASE_URL)
        login_page.login("locked_out_user", "secret_sauce")

        error = page.locator("[data-test='error']")
        expect(error).to_be_visible()
        expect(error).to_contain_text("Sorry, this user has been locked out")

        screenshot.take_screenshot(page, "locked_out_user_error")