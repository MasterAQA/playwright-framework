import time
import allure

from pages.base_page import BasePage


class StorePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._airpods_link = page.locator("//a[@class='rf-productnav-card-title'][contains(text(), 'AirPods')]")
        self._first_product_buy = page.locator("//section[2]//li[1]/div//a")
        self.cart_review = page.locator("//h1[@class='rs-bag-header']")
        self._buy_product = page.locator("//a[@class='icon-wrapper button button-elevated buy']")
        self._button_add_to_cart = page.get_by_text("Add to Bag")

    @allure.step
    def get_page(self):
        self.page.goto(self.base_page + "store")

    @allure.step
    def go_to_category_airpods(self):
        self.find_element(self._airpods_link).click()

    @allure.step
    def buy_product(self):
        self.find_element(self._buy_product).click()

    @allure.step
    def add_to_cart(self):
        self.find_element(self._button_add_to_cart).click()

    @allure.step
    def wait_cart(self):
        self.find_element(self.cart_review)

    @allure.step
    def pause(self, x):
        time.sleep(x)
