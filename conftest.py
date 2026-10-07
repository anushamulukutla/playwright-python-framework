import pytest

from pages.login_page import LoginPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD
import pytest

from playwright.sync_api import sync_playwright
@pytest.fixture
def logged_in_page(page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    return page

@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        yield page

        browser.close()