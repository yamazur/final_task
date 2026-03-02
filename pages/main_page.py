from telnetlib import EC

import allure
from selenium.webdriver.support.wait import WebDriverWait

from config import DEFAULT_TIMEOUT
from pages.base_page import BasePage
from pages.locators import Locators


class MainPage(BasePage):

    URL = "https://www.way2automation.com/"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step('Проверка наличия элементов главной страницы')
    def should_be_elements_in_main_page(self):
        self.is_element_present(
            Locators.HEADER,
            Locators.HORIZONTAL_MENU,
            Locators.CERTIFICATION_BLOCK,
            Locators.BLOCK_OF_COURSES,
            Locators.FOOTER
        )
        return self

    @allure.step('Отображение основного меню в шапке при скроллинге')
    def check_menu_after_scroll(self):
        self.scroll_to_bottom()
        menu = self.wait_for_element(Locators.SITE_NAVIGATION)
        assert menu.is_displayed(), "Меню не отображается после скролла"
        return self

    @allure.step('Клик на раздел Resources в меню')
    def resources_click(self):
        self.wait_and_click(Locators.RESOURCES_BUTTON)
        return self

    @allure.step('Клик на Practice Site1')
    def practice_site1_click(self):
        self.wait_and_click(Locators.PRACTICE_SITE_1_BUTTON)
        return self

    @allure.step('Проверка наличия и клик на навигационную ссылку YouTube')
    def youtube_check_and_click(self):
        self.wait_for_element(Locators.YOUTUBE_BUTTON)
        self.wait_and_click(Locators.YOUTUBE_BUTTON)
        return self

    @allure.step('Проверка перехода на YouTube')
    def check_youtube_url(self):
        WebDriverWait(self.browser, DEFAULT_TIMEOUT).until(
            EC.url_contains("youtube.com")
        )
        assert "youtube.com" in self.browser.current_url, \
            f"Не перешли на YouTube. Текущий URL: {self.browser.current_url}"
        return self
