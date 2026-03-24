import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_TIMEOUT
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
from selenium.webdriver.chrome.options import Options
from pages.sql_login_page import SqlLoginPage

GRID_URL = "http://192.168.31.101:4444"

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

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

@pytest.fixture
def open_sql_login_page(browser):
    page = SqlLoginPage(browser)
    page.open_page_and_checking_url()
    return page

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
