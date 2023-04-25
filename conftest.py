import allure
from playwright.sync_api import sync_playwright, Page
import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.store_page import StorePage


# @pytest.fixture(scope="session")
# def get_playwright():
#     with sync_playwright() as playwright:
#         yield playwright
#
#
# def pytest_generate_tests(metafunc):
#     if "get_browser" in metafunc.fixturenames:
#
#         # metafunc.parametrize("get_browser", metafunc.config.getini("browsers"), indirect=True)
#         metafunc.parametrize("get_browser", metafunc.config.getoption("--browsers"), indirect=True)


# @pytest.fixture(scope="session")
# def get_browser(get_playwright, request):
#     browser = request.param
#     # save browser type to env variable so fixtures and tests can get current browser
#     # Needed to skip unused browser-test combinations
#     os.environ["PWBROWSER"] = browser
#     headless = request.config.getini("headless")
#     if headless == "True":
#         headless = True
#     else:
#         headless = False
#
#     if "chromium" in browser:
#         bro = get_playwright.chromium.launch(headless=headless)
#     elif "firefox" in browser:
#         bro = get_playwright.firefox.launch(headless=headless)
#     elif "webkit" in browser:
#         bro = get_playwright.webkit.launch(headless=headless)
#     else:
#         assert False, "unsupported browser type"
#
#     yield bro
#     bro.close()
#     del os.environ["PWBROWSER"]



@pytest.fixture(scope="function")
def get_page(page: Page, request):
    # context = get_browser.new_context()
    # context.set_default_timeout(20000)
    # page = context.new_page()
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    screenshot = page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)
    allure.attach(screenshot, name=f"{request.node.name}", attachment_type=allure.attachment_type.PNG)
    # video = page.video.path()

    # screenshot = page.screenshot(path=f"screenshots/{request.node.name}.png", full_page=True)


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


def pytest_addoption(parser):
    parser.addini("headless", help="run browser in headless mode", default="True")
    # parser.addini("browsers", help="run browsers", default=["chromium", "firefox", "webkit"])
    # parser.addoption(
    #     "--browsers", action="append", default=[], help="list of stringinputs to pass to test functions",
    # )
