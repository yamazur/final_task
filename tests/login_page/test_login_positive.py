import allure
from allure_commons.types import Severity


class TestLoginPositive:

    @allure.epic("Authentication")
    @allure.feature("Login")
    @allure.story("Login with valid credentials")
    @allure.severity(Severity.CRITICAL)
    def test_login_positive(self, open_login_page):
        (open_login_page
         .login("angular", "password", "angular")
         .check_successful_login_message()
         .logout()
         )
