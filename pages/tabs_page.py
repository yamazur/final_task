import allure

from pages.base_page import BasePage
from pages.locators import Locators


class TabsPage(BasePage):

    URL = "https://way2automation.com/way2auto_jquery/frames-and-windows.php#load_box"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    @allure.step('Открываем три вкладки')
    def opening_new_tabs(self, tabs_count=2):

        iframe = self.wait_for_element(Locators.IFRAME)
        self.browser.switch_to.frame(iframe)

        for _ in range(tabs_count):
            self.wait_and_click(Locators.TABS_LINK)
            new_window = self.browser.window_handles[-1]
            self.browser.switch_to.window(new_window)

