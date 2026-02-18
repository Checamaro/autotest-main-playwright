import pytest
from playwright.sync_api import sync_playwright
from config import settings

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session", params=settings.BROWSERS)
def browser(playwright, request):
    """
    Fixture для запуска теста на каждом браузере из settings.BROWSERS.
    Локально запускается сразу на всех браузерах,
    в GitHub Actions через matrix будет выбран один браузер.
    """
    browser_name = request.param
    browser = getattr(playwright, browser_name).launch(headless=settings.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page