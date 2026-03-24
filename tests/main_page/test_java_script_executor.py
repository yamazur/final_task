import allure
from allure_commons.types import Severity


class TestJavaScriptExecutor:

    @allure.epic("Main Page")
    @allure.feature("JavaScriptExecutor")
    @allure.story("Scroll on page and remove focus from input field")
    @allure.severity(Severity.CRITICAL)
    def test_main_page_load(self, open_main_page):
        (open_main_page
         .close_banner_if_exists()
         .scroll_to_bottom()
         .scroll_to_top()
         .go_to_member_login()
         .click_email_input()
         .remove_focus_from_input()
         )
