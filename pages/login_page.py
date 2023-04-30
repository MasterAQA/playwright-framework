from locators.loc_login_page import Button, Input, Text
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._go_to_sign_in = page.locator("//a[@class='form-button']")
        self._email_input = page.locator("//input[@id='account_name_text_field']")
        self._password_input = page.get_by_placeholder("Password")
        self.identity_two_factor_auth = page.get_by_text("Two-Factor Authentication")

    @property
    def sign_in(self) -> Button:
        return Button(
            self.page.locator("//a[@class='form-button']"),
            "Sign In",
        )

    @property
    def account_input(self) -> Input:
        return Input(
            self.page.locator("//input[@id='account_name_text_field']"),
            "Account input",
        )

    @property
    def password_input(self) -> Input:
        return Input(
            self.page.locator("//input[@id='password_text_field']"),
            "Password input",
        )

    @property
    def two_factor_auth(self) -> Text:
        return Text(
            self.page.get_by_text("message with a verification code"),
            "Two-Factor-Authentication",
        )
