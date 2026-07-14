from pages.login_page import LoginPage
from pages.project_page import ProjectPage
from utils.browser_factory import BrowserFactory
from utils.config import BASE_URL


def test_multi_tenant_access():

    playwright, browser = BrowserFactory.create()

    page = browser.new_page()

    login = LoginPage(page)

    project = ProjectPage(page)

    login.navigate(f"{BASE_URL}/login")

    login.login(
        "admin@company2.com",
        "password123"
    )

    assert project.verify_project_exists(
        "Company2 Project"
    )

    browser.close()

    playwright.stop()
