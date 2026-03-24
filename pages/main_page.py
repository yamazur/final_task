import time

from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from config import DEFAULT_TIMEOUT
from pages.base_page import BasePage
from pages.locators import Locators
from pages.member_login_page import MemberLoginPage


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

    @allure.step('Проверка работы слайдера в блоке с курсами')
    def check_slider_works(self):
        first_title = self.wait_for_element(Locators.FIRST_SLIDE_TITLE)
        title_before = first_title.text

        self.wait_and_click(Locators.SLIDER_NEXT_BUTTON)
        time.sleep(1)  #ждем анимацию

        #проверяем что название изменилось
        new_title = self.wait_for_element(Locators.FIRST_SLIDE_TITLE)
        title_after = new_title.text

        assert title_before != title_after, \
            f"Слайдер не работает: название не изменилось ('{title_before}')"

        return self

    @allure.step('Закрыть баннер если он появился')
    def close_banner_if_exists(self):
        try:
            if self.is_element_present(Locators.BANNER):  # используем timeout по умолчанию
                self.wait_and_click(Locators.BANNER_CLOSE_BUTTON)
                self.is_not_element_present(Locators.BANNER)  # используем timeout по умолчанию
        except TimeoutException:
            pass

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
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        return self

    @allure.step('Проверка перехода на YouTube')
    def check_youtube_url(self):
        WebDriverWait(self.browser, DEFAULT_TIMEOUT).until(
            EC.url_contains("youtube.com")
        )
        assert "youtube.com" in self.browser.current_url, \
            f"Не перешли на YouTube. Текущий URL: {self.browser.current_url}"
        return self

    @allure.step('Переходим в раздел Member Login')
    def go_to_member_login(self):
        self.wait_and_click(Locators.MEMBER_LOGIN_BUTTON)
        return MemberLoginPage(self.browser)
