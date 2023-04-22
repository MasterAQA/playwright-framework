import time

import allure

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.remove_product_button = page.locator("//button[contains(@id, 'delete')]")
        # self.empty_cart = page.locator("//div[contains(@class,'paragraph')]/h1")
        # self.count_product = page.locator("//div[@class='cart-quantity']")
        self.empty_cart = page.locator("//h1[@class='rs-bag-header'][contains(text(), 'Your bag is empty')]")

    @allure.step
    def get_page(self):
        self.page.goto(self.base_page + "shop/bag")


    @allure.step
    def remove_product(self):
        self.find_element(self.remove_product_button).click()

        # self.page.wait_for_selector("//div[@class='cx-item-list-row ng-star-inserted'][1]//button[@class='cart-action-button ng-star-inserted']/img", timeout=30000).click()

    @allure.step
    def wait_empty_cart(self):
        self.find_element(self.empty_cart, 30000)
        # self.page.wait_for_selector("//div[contains(@class,'paragraph')]/h1", timeout=30000, state='attached')
