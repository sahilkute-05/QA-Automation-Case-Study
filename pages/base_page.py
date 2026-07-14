from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def get_text(self, locator):
        return self.page.locator(locator).text_content()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_element(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def take_screenshot(self, filename):
        self.page.screenshot(path=filename)
