import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @allure.step
    def get_page(self):
        self.page.goto("https://www.razer.com/")

    @allure.step
    def wait_elements(self):
        self.page.wait_for_selector('//app-razer-navigation-ui/nav/ul/li', timeout=30000)