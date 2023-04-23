import os

import allure
from playwright.sync_api import sync_playwright
import pytest

from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.store_page import StorePage


@pytest.fixture(scope="session")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session", params=["chromium", "firefox", "webkit"])
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
def get_page(get_browser, request):
    context = get_browser.new_context()
    context.set_default_timeout(20000)
    page = context.new_page()
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    # screenshot = page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    # video = page.video.path()
    # allure.attach(screenshot, name=f"{request.node.name}", attachment_type=allure.attachment_type.PNG)
    # allure.attach.file(f'./{video}', attachment_type=allure.attachment_type.WEBM)

    page.close()
    page.context.tracing.stop(path="reports/trace.zip")




# @pytest.fixture(scope="function")
# def screen_and_video(get_page, request):
#     # yield get_page
#     screenshot = get_page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
#     video = get_page.video.path()
#     allure.attach(screenshot, name=f"{request.node.name}", attachment_type=allure.attachment_type.PNG)
#     allure.attach.file(f'./{video}', attachment_type=allure.attachment_type.WEBM)

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
    parser.addini("headless", help="run browser in headless mode", default="True")




