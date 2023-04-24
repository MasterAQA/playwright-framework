import allure
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def screenshot(main_page, request):
    yield main_page

    screenshot = main_page.page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )


main_directories = [
    "Store",
    "Mac",
    "iPad",
    "iPhone",
    "Watch",
    "AirPods",
    "TV and Home",
    "Entertainment",
    "Accessories",
    "Support",
]


@allure.feature("Main Page")
@allure.story("Main Page")
@allure.title("Test all directories displays")
def test_main_menu(main_page, screenshot):
    main_page.get_page()

    for directory in main_directories:
        expect(main_page.check_category(directory)).to_be_visible()


@allure.feature("Main Page")
@allure.story("Search")
@allure.title("Test search function")
def test_search_function_on_main_page(main_page, screenshot):
    main_page.get_page()
    main_page.click_search_input()
    main_page.search_fill_and_browse("iPhone")

    expect(main_page.results_search).to_be_visible()
