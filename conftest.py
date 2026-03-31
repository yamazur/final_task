import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config import DEFAULT_TIMEOUT
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
from selenium.webdriver.chrome.options import Options
from pages.sql_login_page import SqlLoginPage
from driver_factory import DriverFactory


import os

GRID_URL = os.getenv("GRID_URL", "http://localhost:4444")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--remote", action="store_true")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    is_remote = request.config.getoption("--remote")

    driver = DriverFactory.create_driver(
        browser_name=browser_name,
        is_remote=is_remote,
        grid_url=GRID_URL if is_remote else None
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

@pytest.fixture(autouse=True)
def clean_browser(browser):
    browser.delete_all_cookies()