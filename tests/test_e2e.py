import time

import allure
from playwright.sync_api import expect

# @allure.feature("E2E")
# @allure.story("E2E")
# @allure.title("Login, add and remove from cart")
# def test_e2e(login_page, store_page, cart_page):
#     login_page.get_page()
#     # login_page.reject_cookie_button()
#     login_page.login("sokaya7489@proton.me", "Shftyquweb512")
#     login_page.wait_settings()
#
#     assert login_page.identity_settings.is_visible()
#
#     store_page.get_page()
#     store_page.reject_cookie_button()
#     store_page.click_first_product_buy()
#     store_page.add_to_cart()
#     store_page.wait_review_cart()
#
#     expect(store_page.review_cart_button).to_be_visible()
#
#     time.sleep(1)
#     cart_page.get_page()
#     cart_page.remove_product()
#     cart_page.wait_empty_cart()
#
#     assert cart_page.empty_cart.is_visible()
