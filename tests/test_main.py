import time

import allure
from playwright.sync_api import expect

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
        "Support"
    ]

@allure.feature("Main Page")
@allure.story("Main Page")
@allure.title("Test all directories displays")
def test_main_menu(main_page):
    main_page.get_page()

    for directory in main_directories:
        expect(main_page.check_category(directory)).to_be_visible()

@allure.feature("Main Page")
@allure.story("Search")
@allure.title("Test search function")
def test_searcg(main_page):
    main_page.get_page()
    main_page.click_search_input()
    main_page.search_fill_and_browse("iPhone")

    expect(main_page.results_search).to_be_visible()

# @allure.feature("Main Page")
# @allure.story("Main Page")
# @allure.title("Test all directories displays")
# def test_main_menu(main_page):
#     main_page.get_page()
#
#     for directory in main_directories:
#         main_page.check_category(directory).hover()
#         time.sleep(2)
#
#         expect(main_page.check_sub_category()).to_be_visible()


