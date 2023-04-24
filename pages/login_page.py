import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._go_to_sign_in = page.locator("//a[@class='form-button']")
        self._email_input = page.locator("//input[@id='account_name_text_field']")
        self._password_input = page.get_by_placeholder("Password")
        self.identity_two_factor_auth = page.get_by_text("Two-Factor Authentication")

    @allure.step
    def go_to_sign_in_page(self):
        self.page.goto(self.base_page + "shop/bag")
        self.find_element(self._go_to_sign_in).click()

    @allure.step('Login user with email: "{email}", password: "{password}"')
    def login(self, email, password):
        login_frame = self.page.frame_locator("//iframe")
        login_frame.locator("//input[@id='account_name_text_field']").click()
        self.page.keyboard.type(email)
        self.page.keyboard.press("Enter")

        login_frame.locator("//input[@id='password_text_field']").click()
        self.page.keyboard.type(password)
        self.page.keyboard.press("Enter")

    @allure.step
    def check_two_factor_auth(self):
        login_frame = self.page.frame_locator("//iframe")
        return self.find_element(
            login_frame.get_by_text("message with a verification code")
        )
