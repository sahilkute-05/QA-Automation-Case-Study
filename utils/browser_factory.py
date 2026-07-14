from playwright.sync_api import sync_playwright


class BrowserFactory:

    @staticmethod
    def create(browser_name="chromium"):

        playwright = sync_playwright().start()

        if browser_name == "firefox":
            browser = playwright.firefox.launch(headless=True)

        elif browser_name == "webkit":
            browser = playwright.webkit.launch(headless=True)

        else:
            browser = playwright.chromium.launch(headless=True)

        return playwright, browser
