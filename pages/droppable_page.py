from pages.base_page import BasePage
from pages.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains

class DroppablePage(BasePage):

    URL = "https://way2automation.com/way2auto_jquery/droppable.php"

    def __init__(self, browser):
        super().__init__(browser, self.URL)

    def drag_n_drop_element_and_text_comparison(self):

        self.switch_to_iframe()

        draggable = self.wait_for_element(Locators.DRAGGABLE)
        droppable = self.wait_for_element(Locators.DROPPABLE)

        before_text = droppable.text

        actions = ActionChains(self.browser)
        actions.drag_and_drop(draggable, droppable).perform()

        after_text = droppable.text

        assert before_text != after_text, f"Текст не изменился"
