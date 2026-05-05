from selenium.common import TimeoutException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import DEFAULT_TIMEOUT
import allure


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(DEFAULT_TIMEOUT)

    @allure.step('Открываем страницу и проверяем URL')
    def open_page_and_checking_url(self):
        self.browser.get(self.url)
        assert self.browser.current_url == self.url, \
            f"Expected URL {self.url}, but got {self.browser.current_url}"
        return self

    @allure.step("Ожидание появления элемента")
    def wait_for_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Проверка наличия элемента(ов)")
    def is_element_present(self, *locators, timeout=DEFAULT_TIMEOUT):
        for locator in locators:
            try:
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            except TimeoutException:
                return False
        return True

    @allure.step("Ожидание кликабельности элемента и клик по элементу")
    def wait_and_click(self, locator, timeout=DEFAULT_TIMEOUT):
        click_element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        click_element.click()
        return self

    @allure.step("Проверяем отсутствие элемента")
    def is_not_element_present(self, locators, timeout=DEFAULT_TIMEOUT):  # абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locators))
        except TimeoutException:
            return True

    @allure.step("Ожидание появления элемента")
    def wait_for_alert(self, timeout=DEFAULT_TIMEOUT):
        return WebDriverWait(self.browser, timeout).until(
            EC.alert_is_present()
        )

    @allure.step('Скролл до конца страницы')
    def scroll_to_bottom(self):
        self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        return self

    @allure.step('Скролл в начало страницы')
    def scroll_to_top(self):
        self.browser.execute_script("window.scrollTo(0, 0);")
        return self

    @allure.step('Проверяем, что URL поменялся')
    def check_url(self):
        assert self.browser.current_url != self.url, \
            f"Expected URL {self.url}, but got {self.browser.current_url}"
        return self

    @allure.step('Ввод текста в поле {locator}')
    def type_text(self, locator, text, clear_first=True):
        element = self.wait_for_element(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)
        return self

    @allure.step('Обновление страницы и закрытие алерта после обновления')
    def refresh(self):
        self.browser.refresh()
        try:
            alert = self.browser.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass