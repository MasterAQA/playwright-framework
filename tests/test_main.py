import allure
from playwright.sync_api import expect

main_directories = [
        "Store",
        "PC",
        "Console",
        "Mobile",
        "Lifestyle",
        "Services",
        "Community",
        "Support",
    ]

@allure.feature("Main Page")
@allure.story("Main Page")
@allure.title("Test all directories displays")
def test_main_menu(main_page):
    main_page.get_page()
    main_page.wait_elements()

    for directory in main_directories:
        expect(main_page.page.locator('//app-razer-navigation-ui/nav/ul/li', has_text=directory)).to_be_visible()
