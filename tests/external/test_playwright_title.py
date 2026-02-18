import pytest
import allure

@pytest.mark.regression
@allure.feature("External site")
@allure.story("Playwright homepage H1 header")
def test_playwright_homepage_h1(playwright_dev_page):
    playwright_dev_page.open()
    playwright_dev_page.check_h1()