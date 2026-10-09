
import pytest_asyncio
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD


@pytest_asyncio.fixture
async def page():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        yield page

        await browser.close()


@pytest_asyncio.fixture
async def login(page):
    await page.goto(BASE_URL)

    login_page = LoginPage(page)
    await login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    return ProductsPage(page)