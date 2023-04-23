import time

import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._email_input = page.locator("//input[@id='input-login-email']")
        self._password_input = page.locator("//input[@id='input-login-password']")
        self.identity_settings = page.locator("//div[1]/h2[@class='account-title title-razer'][2]")



    @allure.step('Login user with email: "{email}", password: "{password}"')
    def login(self, email, password):
        self.page.wait_for_selector("//input[@id='input-login-email']", timeout=30000).fill(email)
        self.page.wait_for_selector("//input[@id='input-login-password']").fill(password)
        self.page.wait_for_selector("//button[@id='btn-log-in']").click()
        self.page.wait_for_url("https://razerid.razer.com/account")

    @allure.step
    def wait_settings(self):
        self.page.wait_for_selector("//div[1]/h2[@class='account-title title-razer'][2]", timeout=30000)


