import allure
from pages.base_page import BasePage
from elements.text import Text

class PlaywrightDevPage(BasePage):

    H1_LOCATOR = "h1.hero__title"
    EXPECTED_H1 = "Playwright enables reliable end-to-end testing for modern web apps."

    @allure.step("Open Playwright website")
    def open(self):
        self.visit("https://playwright.dev/")

    @allure.step("Check H1 header text")
    def check_h1(self):
        h1 = Text(self.page, self.H1_LOCATOR)
        actual = h1.get_text()
        assert actual.strip() == self.EXPECTED_H1, \
            f"Expected H1 '{self.EXPECTED_H1}', got '{actual}'"