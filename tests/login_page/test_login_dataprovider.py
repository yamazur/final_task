import allure
import pytest
from allure_commons.types import Severity


class TestLoginDataProvider:

    @allure.epic("Authentication")
    @allure.feature("Login")
    @allure.story("Login with different credentials")
    @allure.severity(Severity.CRITICAL)

    @pytest.mark.parametrize("username, password, username_description, expected", [
        ("angular", "password", "angular", "success"),
        ("angular", "wrong", "angular", "fail"),
        ("wrong", "password", "angular", "fail"),
    ])
    def test_login_dataprovider(self, open_login_page, username, password, username_description, expected):
        page = (open_login_page.login(username, password, username_description))

        if expected == "success":
            page.check_successful_login_message().logout()
        else:
            page.check_unsuccessful_login()
