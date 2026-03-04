import allure
from allure_commons.types import Severity


class TestMainPageNavigation:

    @allure.epic("Main Page")
    @allure.feature("Navigation")
    @allure.story("Resources → Practice Site 1")
    @allure.severity(Severity.NORMAL)
    def test_main_page_navigation(self, open_main_page):
        open_main_page.resources_click().practice_site1_click().check_url()