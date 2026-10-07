import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD


@pytest.fixture
def login(page):
    page.goto(BASE_URL)

    login_page = LoginPage(page)
    login_page.login(STANDARD_USER, STANDARD_PASSWORD)

    return ProductsPage(page)