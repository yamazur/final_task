import allure

from config import DEFAULT_TIMEOUT
from pages.base_page import BasePage
from pages.locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SqlLoginPage(BasePage):

    URL = "https://www.sql-ex.ru/"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step('Находим элементы для авторизации')
    def should_be_elements_in_sql_login_page(self):
        self.is_element_present(
            Locators.SQL_LOGIN,
            Locators.SQL_PASSWORD,
            Locators.SQL_ENTER_BUTTON
        )
        return self

    @allure.step('Вводим логин и пароль и нажимаем войти')
    def login_sql(self, username, password):
        self.type_text(Locators.SQL_LOGIN, username)
        self.type_text(Locators.SQL_PASSWORD, password)
        self.wait_and_click(Locators.SQL_ENTER_BUTTON)
        return self

    @allure.step('Проверяем, что авторизация прошла успешно')
    def should_be_authorized_sql_user(self):
        assert self.is_not_element_present(Locators.SQL_LOGIN), \
            "Поле ввода логина всё ещё отображается — пользователь не авторизован"
        return self

    @allure.step('Ожидание исчезновения формы SQL-логина после успешного входа')
    def wait_for_login_form_to_disappear(self, timeout=DEFAULT_TIMEOUT):
        WebDriverWait(self.browser, timeout).until(
            EC.invisibility_of_element_located(Locators.SQL_LOGIN)
        )
        return self
