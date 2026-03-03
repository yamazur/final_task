class TestMainPageLoad:
    def test_main_page_load(self, main_page):
        (main_page
            .open_page_and_checking_url()
            .close_banner_if_exists()
            .should_be_elements_in_main_page()
            .check_slider_works()
         )
