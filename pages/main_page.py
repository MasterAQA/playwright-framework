import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.main_category = "//li[@class='globalnav-submenu-trigger-item']//a[contains(@aria-label, '{}')]"
        self._search_button_show = page.locator("//a[@id='globalnav-menubutton-link-search']")
        self._search_input = page.locator("//input[@class='globalnav-searchfield-input']")
        self.results_search = page.locator("//div[@class='rf-serp-resultcount']")
        self.sub_category = page.locator("//li[@class='globalnav-submenu-list-item-elevated'][1]/a")


    @allure.step
    def get_page(self):
        self.page.goto(self.base_page)

    @allure.step
    def check_category(self, category_name):
        return self.find_element(self.page.locator(self.main_category.format(category_name)))

    @allure.step
    def check_sub_category(self):
        return self.find_element(self.sub_category)

    @allure.step
    def click_search_input(self):
        self.find_element(self._search_button_show).click()

    @allure.step
    def search_fill_and_browse(self, search_text):
        self.find_element(self._search_input)
        self._search_input.click()
        self.page.keyboard.type(search_text)
        self.page.keyboard.press('Enter')






