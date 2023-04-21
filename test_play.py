from playwright.sync_api import sync_playwright

from playwright.sync_api import Page

# def test_visit_admin_dashboard(page: Page):
#     page.goto("https://grinfer.com")
#     page.screenshot(path="example.png")

# with sync_playwright() as p:
#     browser = p.chromium.launch()
#     page = browser.new_page()
#     # page.goto("https://grinfer.com")
#     # await page.locator("xpath=//button").click()
#     page.goto("https://www.razer.com/")
#     page.locator("//button[@id='onetrust-reject-all-handler']").click()
#     # page.locator("//button[@id='newsletter-close']").click()
#     # page.get_by_role("a", name="https://www.razer.com/store").click()
#     # page.get_by_text("Store").click()
#     # page.get
#     page.locator("app-razer-generic-link", has_text="Store").click()
#     page.screenshot(path="example.png")
#
#     # await page.get_by_role("button", name="Networking").click()
#     # page.locator("xpath=//button").click()
#     #
#     # page.screenshot(path="example.png")
#     browser.close()


import re
# from playwright.sync_api import Page, expect
#
#
# def test_homepage(page: Page):
#     page.goto("https://us.msi.com")
#
#     # await page.locator("xpath=///div[@class='menuAction__item'][3]/button[text()='comment-content'][contains(text(), '{}')]").click()
#
#     # await page.get_by_text("ODM Solutions").click()
#
#     # expect(page.locator("button")).to_contain_text("Networking")
#
#     page.get_by_role("button", name="Networking").click()
#
#
#
#     # page.get_by_role("span", name="Networking").click()
#     page.screenshot(path="example.png")
    # await page.locator()

    # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    # get_started = page.get_by_role("link", name="Get started")
    #
    # # Expect an attribute "to be strictly equal" to the value.
    # expect(get_started).to_have_attribute("href", "/docs/intro")
    #
    # # Click the get started link.
    # get_started.click()
    #
    # # Expects the URL to contain intro.
    # expect(page).to_have_url(re.compile(".*intro"))