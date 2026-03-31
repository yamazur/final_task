from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions


class DriverFactory:

    @staticmethod
    def create_driver(browser_name: str, is_remote: bool = False, grid_url: str = None):

        browser_name = browser_name.lower()

        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")

            if is_remote:
                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )
            else:
                return webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

            if is_remote:
                return webdriver.Remote(
                    command_executor=grid_url,
                    options=options
                )
            else:
                return webdriver.Firefox(options=options)

        elif browser_name == "safari":
            if is_remote:
                return webdriver.Remote(
                    command_executor=grid_url,
                    options=SafariOptions()
                )
            else:
                return webdriver.Safari()

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
