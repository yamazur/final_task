import allure
from allure_commons.types import Severity


class TestMainPageSocialLinks:

    @allure.epic("Main Page")
    @allure.feature("Social Links")
    @allure.story("YouTube link works correctly")
    @allure.severity(Severity.MINOR)
    def test_main_page_social_links(self, open_main_page):
        open_main_page.youtube_check_and_click().check_url()