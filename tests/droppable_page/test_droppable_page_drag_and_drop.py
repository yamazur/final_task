import allure
from allure_commons.types import Severity


class TestDroppablePageDragAndDrop:

    @allure.epic("Droppable Page")
    @allure.feature("Drag n Drop")
    @allure.story("Drag and drop an element with text change")
    @allure.severity(Severity.MINOR)
    def test_droppable_page_drag_and_drop(self, browser, open_droppable_page):
        open_droppable_page.drag_and_drop_element()
