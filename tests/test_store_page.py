import allure
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def screenshot(store_page, request):
    yield store_page

    screenshot = store_page.page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )


@allure.feature("Cart")
@allure.story("Add in Cart")
@allure.title("Add product in Cart")
def test_add_product(store_page, screenshot):
    store_page.get_page()
    store_page.go_to_category_airpods()
    store_page.buy_product()
    store_page.add_to_cart()
    store_page.wait_cart()

    expect(store_page.cart_review).to_be_visible()


@pytest.mark.flaky(reruns=2)
@allure.feature("Cart")
@allure.story("Add and Remove")
@allure.title("Add product, and remove from Cart")
def test_add_and_remove_product(store_page, cart_page, screenshot):
    store_page.get_page()
    store_page.go_to_category_airpods()
    store_page.buy_product()
    store_page.add_to_cart()
    store_page.wait_cart()

    expect(store_page.cart_review).to_be_visible()

    cart_page.remove_product()
    expect(cart_page.empty_cart).to_be_visible()
