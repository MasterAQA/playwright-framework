import allure
from playwright.sync_api import Page, Locator
from config import base_page


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_page = base_page


    def find_element(self, element: Locator, default_timeout=15000) -> Locator:
        element.wait_for(timeout=default_timeout)
        return element


    @allure.step
    def delete_cookies(self):
        self.page.context.clear_cookies()


    @allure.step
    def reload(self):
        self.page.reload(wait_until="load")


