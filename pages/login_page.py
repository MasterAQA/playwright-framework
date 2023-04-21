import time

import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._email_input = page.locator("//input[@id='input-login-email']")
        self._password_input = page.locator("//input[@id='input-login-password']")
        self.identity_settings = page.locator("//div[1]/h2[@class='account-title title-razer'][2]")




    @allure.step
    def get_page(self):
        self.page.goto("https://razerid.razer.com/", wait_until="load")
        if self._cookie_frame_close.is_visible():
            self._cookie_frame_close.click()

    @allure.step('Login user with email: "{email}", password: "{password}"')
    def login(self, email, password):
        self.page.wait_for_selector("//input[@id='input-login-email']", timeout=30000).fill(email)
        self.page.wait_for_selector("//input[@id='input-login-password']").fill(password)
        self.page.wait_for_selector("//button[@id='btn-log-in']").click()
        self.page.wait_for_url("https://razerid.razer.com/account")

    @allure.step
    def wait_settings(self):
        self.page.wait_for_selector("//div[1]/h2[@class='account-title title-razer'][2]", timeout=30000)


        # self.page.wait_for_selector("//section[2]//li[1]/div//a", timeout=10000).click()
        # self.el(self._first_product_buy).click()
        # time.sleep(2)
        # self._first_product_buy.click()


    # @allure.step
    # def add_to_cart(self):
    #     self.page.wait_for_selector("//button[contains(@id, 'add-to-cart')]", timeout=10000).click()
    #     # self.el(self._button_add_to_cart).click()

