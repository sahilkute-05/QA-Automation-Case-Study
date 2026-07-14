from pages.base_page import BasePage


class DashboardPage(BasePage):

    WELCOME_MESSAGE = ".welcome-message"

    def verify_dashboard_loaded(self):

        self.wait_for_element(self.WELCOME_MESSAGE)
