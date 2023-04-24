import allure
import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="function")
def screenshot(search_page, request):
    yield search_page

    screenshot = search_page.page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )


@allure.feature("Search Page")
@allure.story("Search")
@allure.title("Test search page and function")
def test_search(search_page, screenshot):
    search_page.get_page()
    search_page.search_fill_and_browse("Mac")

    expect(search_page.results_search).to_be_visible()
