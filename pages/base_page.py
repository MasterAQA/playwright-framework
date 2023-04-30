import allure
from playwright.sync_api import Page
from unicodedata import name


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def go_to(self, url: str):
        with allure.step(f"Open {name} page"):
            self.page.goto(url)

    @allure.step
    def delete_cookies(self):
        self.page.context.clear_cookies()

    @allure.step
    def reload(self):
        self.page.reload(wait_until="load")
