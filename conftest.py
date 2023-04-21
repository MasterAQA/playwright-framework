import os
from playwright.sync_api import sync_playwright
import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.store_page import StorePage


@pytest.fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
# @pytest.fixture(scope="session")
# @pytest.fixture(scope="session", params=["chromium"])
def get_browser(get_playwright, request):

    browser = request.param
    # save browser type to env variable so fixtures and tests can get current browser
    # Needed to skip unused browser-test combinations
    os.environ["PWBROWSER"] = browser
    headless = request.config.getini("headless")
    if headless == "True":
        headless = True
    else:
        headless = False

    if browser == "chromium":
        bro = get_playwright.chromium.launch(headless=headless)
    elif browser == "firefox":
        bro = get_playwright.firefox.launch(headless=headless)
    elif browser == "webkit":
        bro = get_playwright.webkit.launch(headless=headless)
    else:
        assert False, "unsupported browser type"

    yield bro
    bro.close()
    del os.environ["PWBROWSER"]


@pytest.fixture(scope="session")
def get_page(get_browser):
    context = get_browser.new_context()
    context.set_default_timeout(30000)
    page = context.new_page()
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page
    page.close()
    page.context.tracing.stop(path="reports/trace.zip")


@pytest.fixture()
def main_page(get_page) -> MainPage:
    return MainPage(get_page)


@pytest.fixture()
# @pytest.mark.parametrize("request", params=["chromium", "firefox"], indirect=['get_browser'])
def store_page(get_page) -> StorePage:
    return StorePage(get_page)

@pytest.fixture()
def login_page(get_page) -> LoginPage:
    return LoginPage(get_page)

@pytest.fixture()
def cart_page(get_page) -> CartPage:
    return CartPage(get_page)


def pytest_addoption(parser):
    # parser.addoption('--secure', action='store', default='secure.json')
    parser.addini("headless", help="run browser in headless mode", default="True")
    # parser.addini('tcm_report', help='report test results to tcm', default='False')



