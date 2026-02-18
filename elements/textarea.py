import allure
from playwright.sync_api import expect
from elements.base_element import BaseElement

class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return 'textarea'

    def fill(self, value: str):
        with allure.step(f'Fill textarea "{value}"'):
            self.locator.fill(value)

    def check_have_value(self, value: str):
        with allure.step(f'Check textarea has value "{value}"'):
            expect(self.locator).to_have_value(value)