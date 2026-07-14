from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = "#email"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login-btn"

    def login(self, email, password):

        self.fill(self.EMAIL, email)

        self.fill(self.PASSWORD, password)

        self.click(self.LOGIN_BUTTON)
