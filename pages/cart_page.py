import allure

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.remove_product_button = page.locator("//button[contains(@id, 'delete')]")
        self.empty_cart = page.locator("//h1[@class='rs-bag-header'][contains(text(), 'Your bag is empty')]")

    @allure.step
    def get_page(self):
        self.page.goto(self.base_page + "shop/bag")

    @allure.step
    def remove_product(self):
        self.find_element(self.remove_product_button).click()
