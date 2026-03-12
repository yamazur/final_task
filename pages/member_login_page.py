import allure

from pages.base_page import BasePage
from pages.locators import Locators


class MemberLoginPage(BasePage):

    @allure.step('Кликаем в поле ввода')
    def click_email_input(self):
        self.wait_and_click(Locators.EMAIL_INPUT)
        return self

    @allure.step("Убираем фокус с поля ввода через JSExecutor")
    def remove_focus_from_input(self):
        self.browser.execute_script("document.activeElement.blur();")
        return self
