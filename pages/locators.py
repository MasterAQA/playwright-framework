import allure
import playwright
from playwright.sync_api import Locator, Page

from pages.base_element import BaseElement
#
#
class Button(BaseElement):

    def __init__(self, selector: playwright.sync_api.Locator, name: str):
        super().__init__(selector, name)


    def click(self):
        with allure.step(f"Click button [{self.name}]"):
            self.selector.click()

#
#
# class Input(BaseElement):
#     def __init__(self, selector):
#         super().__init__(selector)
#
#     def fill(self):
#         with allure.step(f"Click button []"):
#             self.selector.fill()
#
#     def clear(self):
#         with allure.step(f"Click button []"):
#             self.selector.clear()

    # def click(self):
    #     with allure.step(f"Click button [{self.name}]"):
    #         self.selector.click()


# class Button:
#     def __init__(self, locator, page: Page):
#         self.page = page
#         self.locator = locator
#         self.wait_element()
#
#     def wait_element(self):
#         self.page.locator(self.locator).wait_for()
#
#     def click(self):
#         self.page.locator(self.locator).click()
#
#     def screenshot(self):
#         self.page.locator(self.locator).screenshot()
