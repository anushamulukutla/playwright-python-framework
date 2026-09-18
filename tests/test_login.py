from pages.login_page import LoginPage
from test_data.users import BASE_URL, STANDARD_USER, STANDARD_PASSWORD

class TestLogin:
    def test_login(self, page):
        login_page = LoginPage(page)
        page.goto(BASE_URL)
        login_page.login(STANDARD_USER, STANDARD_PASSWORD)
        assert page.url == f"{BASE_URL}/inventory.html"
