import pytest
from playwright.sync_api import Page
from pages.external.playwright_dev_page import PlaywrightDevPage

@pytest.fixture
def playwright_dev_page(page: Page) -> PlaywrightDevPage:
    """
    Возвращает объект страницы PlaywrightDevPage
    """
    return PlaywrightDevPage(page=page)