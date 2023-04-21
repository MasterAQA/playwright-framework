# from pages.web_elements import *
import time

import allure
from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self._cookie_frame_close = page.locator("//button[@id='onetrust-reject-all-handler']")


    def find_element(self, element: Locator, default_timeout=10000) -> Locator:
        self.cookie_frame()
        element.wait_for(timeout=default_timeout)
        self.cookie_frame()
        return element

    def cookie_frame(self):
        if self._cookie_frame_close.is_visible():
            self._cookie_frame_close.click()
            time.sleep(1)

    @allure.step
    def delete_cookies(self):
        self.page.context.clear_cookies()


    @allure.step
    def reload(self):
        self.page.reload(wait_until="load")

    @allure.step
    def reject_cookie_button(self):
        self.page.wait_for_selector("//button[@id='onetrust-reject-all-handler']", timeout=10000).click()
        # self._cookie_frame_close.click()
