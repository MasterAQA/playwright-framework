import allure
import playwright.sync_api
from playwright.sync_api import expect


class BaseElement:
    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        self.selector = selector
        self.name = name

    def wait_to_be_visible(self):
        with allure.step(f"Wait until [{self.name}] is visible"):
            expect(self.selector).to_be_visible()

    def check_is_visible(self):
        with allure.step(f"Check what [{self.name}] is visible"):
            expect(self.selector).to_be_visible()
