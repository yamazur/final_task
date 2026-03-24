import time

import allure
from allure_commons.types import Severity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import SQL_LOGIN, SQL_PASSWORD, DEFAULT_TIMEOUT
from pages.cookies_helper import save_cookies, load_cookies
from pages.locators import Locators


class TestSqlLoginPageWithCookies:

    @allure.epic("SQL-EX")
    @allure.feature("Authorization")
    @allure.story("Login with cookies")
    @allure.severity(Severity.CRITICAL)
    def test_sql_login_page_with_cookies(self, browser, open_sql_login_page):
        (open_sql_login_page
         .should_be_elements_in_sql_login_page()
         .login_sql(SQL_LOGIN, SQL_PASSWORD)
         .wait_for_login_form_to_disappear()
         .should_be_authorized_sql_user())

        save_cookies(browser, "cookies.json")

        browser.delete_all_cookies()
        browser.refresh()

        # проверяем, что пользователь действительно разлогинился
        open_sql_login_page.should_be_elements_in_sql_login_page()

        load_cookies(browser, "cookies.json")
        browser.refresh()

        open_sql_login_page.should_be_authorized_sql_user()
