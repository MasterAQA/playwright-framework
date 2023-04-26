import allure
from playwright.sync_api import Page
import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


@pytest.fixture(scope="function")
def get_page(page: Page, request):
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    screenshot = page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )

    page.close()
    page.context.tracing.stop(path="reports/trace.zip")


@pytest.fixture()
def main_page(get_page) -> MainPage:
    return MainPage(get_page)


@pytest.fixture()
def store_page(get_page) -> StorePage:
    return StorePage(get_page)


@pytest.fixture()
def login_page(get_page) -> LoginPage:
    return LoginPage(get_page)


@pytest.fixture()
def cart_page(get_page) -> CartPage:
    return CartPage(get_page)


@pytest.fixture()
def search_page(get_page) -> SearchPage:
    return SearchPage(get_page)
