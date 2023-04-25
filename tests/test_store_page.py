import allure
import pytest
from playwright.sync_api import expect

@pytest.mark.only_browser("firefox")
@allure.feature("Cart")
@allure.story("Add in Cart")
@allure.title("Add product in Cart")
def test_add_product(store_page):
    store_page.get_page()
    store_page.go_to_category_airpods()
    store_page.buy_product()
    store_page.add_to_cart()
    store_page.wait_cart()

    expect(store_page.cart_review).to_be_visible()

@pytest.mark.only_browser("firefox")
@pytest.mark.flaky(reruns=2)
@allure.feature("Cart")
@allure.story("Add and Remove")
@allure.title("Add product, and remove from Cart")
def test_add_and_remove_product(store_page, cart_page):
    store_page.get_page()
    store_page.go_to_category_airpods()
    store_page.buy_product()
    store_page.add_to_cart()
    store_page.wait_cart()

    expect(store_page.cart_review).to_be_visible()

    cart_page.remove_product()
    expect(cart_page.empty_cart).to_be_visible()
