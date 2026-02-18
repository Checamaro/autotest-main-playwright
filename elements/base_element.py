class BaseElement:

    def __init__(self, page, locator: str):
        self.locator = page.locator(locator)

    def click(self):
        self.locator.click()

    def get_text(self):
        return self.locator.text_content()