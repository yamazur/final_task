import allure
from faker import Faker

from pages.base_page import BasePage
from pages.locators import Locators


class LoginPage(BasePage):

    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step('Заполняем поля и нажимаем на кнопку Login')
    def login(self, username, password, username_description):
        self.type_text(Locators.USERNAME_INPUT, username)
        self.type_text(Locators.PASSWORD_INPUT, password)
        self.type_text(Locators.USERNAME_DESCRIPTION_INPUT, username_description)

        self.wait_and_click(Locators.LOGIN_BUTTON)

        return self

    @allure.step('Проверяем, что авторизация прошла успешно')
    def check_successful_login_message(self):
        message_element = self.wait_for_element(Locators.SUCCESS_MESSAGE)
        assert message_element.text == "You're logged in!!", \
            f"Ожидался текст 'You're logged in!!', получен '{message_element.text}'"
        return self

    @allure.step('Выходим из аккаунта')
    def logout(self):
        self.wait_and_click(Locators.LOGOUT_LINK)
        return self

    @allure.step('Проверяем, что авторизация не прошла')
    def check_unsuccessful_login(self):
        error_message = self.wait_for_element(Locators.ERROR_MESSAGE)
        assert error_message.text == "Username or password is incorrect", \
            f"Ожидался текст 'Username or password is incorrect', получен '{error_message.text}'"
        return self
