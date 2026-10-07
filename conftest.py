import pytest_asyncio
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD


@pytest_asyncio.fixture
async def login():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(BASE_URL)

        login_page = LoginPage(page)
        await login_page.login(STANDARD_USER, STANDARD_PASSWORD)

        yield ProductsPage(page)

        await browser.close()

# import pytest
# from pages.login_page import LoginPage
# from pages.products_page import ProductsPage
# from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD


# @pytest.fixture
# def login(page):
#     page.goto(BASE_URL)

#     login_page = LoginPage(page)
#     login_page.login(STANDARD_USER, STANDARD_PASSWORD)

#     return ProductsPage(page)

