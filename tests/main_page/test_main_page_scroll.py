import allure
from allure_commons.types import Severity


class TestMainPageScroll:

    @allure.epic("Main Page")
    @allure.feature("Menu")
    @allure.story("Menu stays visible on scroll")
    @allure.severity(Severity.MINOR)
    def test_main_page_scroll(self, open_main_page):
        open_main_page.check_menu_after_scroll()