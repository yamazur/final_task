import allure
from faker import Faker

from pages.base_page import BasePage
from pages.locators import Locators


class LoginPage(BasePage):

    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step('Заполняем все поля валидно')
    def fill_fields_with_valid_data(self):

        self.type_text(Locators.USERNAME_INPUT, "angular")
        self.type_text(Locators.PASSWORD_INPUT, "password")
        self.type_text(Locators.USERNAME_DESCRIPTION_INPUT, "angular")

        return self

    @allure.step('Кликаем на кнопку Login')
    def login_click(self):
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

    @allure.step('Заполяем только два поля валидно')
    def fill_fields_with_invalid_data(self):
        fake = Faker()

        self.type_text(Locators.USERNAME_INPUT, fake.user_name())
        self.type_text(Locators.PASSWORD_INPUT, "password")
        self.type_text(Locators.USERNAME_DESCRIPTION_INPUT, fake.user_name())

        return self

    @allure.step('Проверяем, что авторизация не прошла')
    def check_unsuccessful_login(self):
        error_message = self.wait_for_element(Locators.ERROR_MESSAGE)
        assert error_message.text == "Username or password is incorrect", \
            f"Ожидался текст 'Username or password is incorrect', получен '{error_message.text}'"
        return self
