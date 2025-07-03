from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope='session')
def management_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
                                    # args=["--start-maximized"]
                                    )

        yield browser
        browser.close()


@pytest.fixture(scope='function')
def open_page(management_browser):
    page = management_browser.new_page()
    yield page
    page.close()
