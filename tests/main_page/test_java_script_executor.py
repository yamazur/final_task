class TestJavaScriptExecutor:
    def test_main_page_load(self, open_main_page):
        (open_main_page
         .close_banner_if_exists()
         .scroll_to_beginning()
         .scroll_to_top()
         .go_to_member_login()
         .click_email_input()
         .remove_focus_from_input()
         )
