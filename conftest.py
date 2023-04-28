import allure
from playwright.sync_api import Page
import pytest


@pytest.fixture(scope="function")
def get_page(page: Page, request):
    page.context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    screenshot = page.screenshot(
        path=f"screenshots/{request.node.name}.png", full_page=True
    )
    allure.attach(
        screenshot,
        name=f"{request.node.name}",
        attachment_type=allure.attachment_type.PNG,
    )

    page.close()
    page.context.tracing.stop(path="reports/trace.zip")


