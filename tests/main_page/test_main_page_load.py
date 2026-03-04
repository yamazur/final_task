import allure
from allure_commons.types import Severity


class TestMainPageLoad:

    @allure.epic("Main Page")
    @allure.feature("Page Load")
    @allure.story("Page loading and URL correctness, visibility of page elements and slider operation")
    @allure.severity(Severity.CRITICAL)
    def test_main_page_load(self, open_main_page):
        (open_main_page
            .close_banner_if_exists()
            .should_be_elements_in_main_page()
            .check_slider_works()
         )
