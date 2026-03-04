import allure
from allure_commons.types import Severity


class TestLoginNegative:

    @allure.epic("Authentication")
    @allure.feature("Login")
    @allure.story("Login with invalid credentials")
    @allure.severity(Severity.NORMAL)
    def test_login_negative(self, open_login_page):
        (open_login_page
         .fill_fields_with_invalid_data()
         .login_click()
         .check_unsuccessful_login()
         )
