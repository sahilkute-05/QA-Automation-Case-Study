from pages.base_page import BasePage


class ProjectPage(BasePage):

    PROJECT_CARD = ".project-card"

    def verify_project_exists(self, project_name):

        projects = self.page.locator(self.PROJECT_CARD)

        count = projects.count()

        for i in range(count):

            text = projects.nth(i).text_content()

            if project_name in text:

                return True

        return False
