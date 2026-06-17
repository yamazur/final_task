import allure
from allure_commons.types import Severity


class TestTabsPage:

    @allure.epic("Tabs Page")
    @allure.feature("Opening new tabs")
    @allure.story("Opening new tabs via a link")
    @allure.severity(Severity.NORMAL)
    def test_tabs_page(self, browser, open_tabs_page):
        open_tabs_page.opening_new_tabs()

        assert len(browser.window_handles) == 3, \
            f"Expected 3 windows, got {len(browser.window_handles)}"
