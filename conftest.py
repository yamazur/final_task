import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_TIMEOUT
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, DEFAULT_TIMEOUT)  #явное ожидание

@pytest.fixture
def open_main_page(browser):
    page = MainPage(browser)
    page.open_page_and_checking_url()
    return page

@pytest.fixture
def open_login_page(browser):
    page = LoginPage(browser)
    page.open_page_and_checking_url()
    return page

import pytest
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")

        if driver:
            screenshot = driver.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name=f"screenshot_{item.name}",
                attachment_type=allure.attachment_type.PNG
            )
