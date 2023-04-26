import allure
import pytest
from playwright.sync_api import expect
from config import apple_username, apple_password


@pytest.mark.only_browser("chromium")
@pytest.mark.flaky(reruns=2)
@allure.feature("Login")
@allure.story("Login")
@allure.title("Login in Apple account, check two-factor auth")
def test_login(login_page):
    login_page.go_to_sign_in_page()
    login_page.login(apple_username, apple_password)

    expect(login_page.check_two_factor_auth()).to_be_visible()
