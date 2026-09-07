#
import re
from playwright.sync_api import Playwright, sync_playwright, expect


class TestMainPage:
    def test_create_todo(self, playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.get_by_role("link", name="real TodoMVC app.").click()
        with page.expect_download() as download_info:
            page.get_by_role("link", name="Download").click()
        download = download_info.value
        page.get_by_role("link", name="React New", exact=True).click()
        page.get_by_test_id("text-input").click()
        page.get_by_test_id("text-input").fill("hi")
        page.get_by_test_id("text-input").press("Enter")

        # ---------------------
        context.close()
        browser.close()


# playwright codegen demo.playwright.dev/todomvc/#/