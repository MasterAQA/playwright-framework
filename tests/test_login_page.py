import allure
from playwright.sync_api import expect

@allure.feature("Login")
@allure.story("Login")
@allure.title("Login in Razer account")
def test_login(login_page):
    login_page.get_page()
    login_page.reject_cookie_button()
    login_page.login("sokaya7489@proton.me", "Shftyquweb512")
    login_page.wait_settings()

    assert login_page.identity_settings.is_visible()
    # expect(login_page.review_cart_button).to_be_visible()