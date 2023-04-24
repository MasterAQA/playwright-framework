import allure

from pages.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._search_input = page.locator("//input[@id='searchform-input']")
        self.results_search = page.locator("//div[@class='rf-serp-resultcount']")

    @allure.step
    def get_page(self):
        self.page.goto(self.base_page + "us/searchj")

    @allure.step
    def search_fill_and_browse(self, search_text):
        self.find_element(self._search_input)
        self._search_input.click()
        self.page.keyboard.type(search_text)
        self.page.keyboard.press("Enter")
