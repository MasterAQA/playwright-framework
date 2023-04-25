import allure
import pytest
from playwright.sync_api import expect


@pytest.mark.only_browser("firefox")
@allure.feature("Search Page")
@allure.story("Search")
@allure.title("Test search page and function")
def test_search(search_page):
    search_page.get_page()
    search_page.search_fill_and_browse("Mac")

    expect(search_page.results_search).to_be_visible()
