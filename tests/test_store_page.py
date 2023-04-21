import random
import time

import allure
import pytest
from playwright.sync_api import expect


@allure.feature("Cart")
@allure.story("Add in Cart")
@allure.title("Add product in Cart")
def test_add_product(store_page):
    store_page.get_page()
    # store_page.reject_cookie_button()
    store_page.click_first_product_buy()
    store_page.add_to_cart()

    expect(store_page.review_cart_button).to_be_visible()


@pytest.mark.flaky(reruns=2)
@allure.feature("Cart")
@allure.story("Add and Remove")
@allure.title("Add product, and remove from Cart")
def test_add_and_remove_product(store_page, cart_page):
    store_page.get_page()
    # store_page.reject_cookie_button()
    store_page.click_first_product_buy()
    store_page.add_to_cart()
    store_page.wait_review_cart()

    expect(store_page.review_cart_button).to_be_visible()

    # store_page.pause(2)
    # time.sleep(random.randint(1, 20))
    time.sleep(1)
    cart_page.get_page()
    # time.sleep(5)
    cart_page.remove_product()
    cart_page.wait_empty_cart()

    assert cart_page.empty_cart.is_visible()

    # expect(cart_page.empty_cart).
