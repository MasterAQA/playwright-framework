import time

import allure

from pages.base_page import BasePage


class StorePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._first_product_buy = page.locator("//section[2]//li[1]/div//a")
        self._button_add_to_cart = page.locator("//button[contains(@id, 'add-to-cart')]")
        self.review_cart_button = page.get_by_role("button", name="Review Cart")

    @allure.step
    def get_page(self):
        self.page.goto("https://www.razer.com/store", wait_until='load')
        time.sleep(1)


    @allure.step
    def click_first_product_buy(self):
        self.find_element(self._first_product_buy).click()
        # self.page.wait_for_selector("//section[2]//li[1]/div//a", timeout=30000).click()


    @allure.step
    def add_to_cart(self):
        self.find_element(self._button_add_to_cart).click()
        # self.page.wait_for_selector("//button[contains(@id, 'add-to-cart')]", timeout=30000).click()


    @allure.step
    def wait_review_cart(self):
        self.find_element(self.review_cart_button)

    @allure.step
    def pause(self, x):
        time.sleep(x)

