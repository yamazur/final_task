from selenium import webdriver

class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str):
        if browser_name == "chrome":
            return webdriver.Chrome()

        elif browser_name == "firefox":
            return webdriver.Firefox()

        elif browser_name == "safari":
            return webdriver.Safari()

        # elif browser_name == "ie":
        #     from selenium.webdriver.ie.options import Options
        #     options = Options()
        #     options.ignore_zoom_level = True
        #     options.ignore_protected_mode_settings = True
        #     return webdriver.Ie(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")