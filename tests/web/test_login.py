from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.browser_factory import BrowserFactory
from utils.config import BASE_URL


def test_login():

    playwright, browser = BrowserFactory.create()

    page = browser.new_page()

    login = LoginPage(page)
    dashboard = DashboardPage(page)

    login.navigate(f"{BASE_URL}/login")

    login.login(
        "admin@company1.com",
        "password123"
    )

    dashboard.verify_dashboard_loaded()

    browser.close()
    playwright.stop()
