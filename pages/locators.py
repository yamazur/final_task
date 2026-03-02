from selenium.webdriver.common.by import By


class Locators:

    #главная страница
    #тест-кейс 1
    HEADER = (By.CSS_SELECTOR, ".ast-above-header-bar")
    HORIZONTAL_MENU = (By.ID, "ast-hf-menu-1")
    CERTIFICATION_BLOCK = (By.CSS_SELECTOR, ".elementor-element-5b4952c1")
    BLOCK_OF_COURSES = (By.ID, "166618a")
    COURSES_BUTTON = (By.CSS_SELECTOR, ".swiper-button-next-c50f9f0")
    FOOTER = (By.CSS_SELECTOR, ".elementor-element-4cfa36e1")

    #тест-кейс 2
    SITE_NAVIGATION = (By.ID, "site-navigation")

    #тест-кейс 3
    RESOURCES_BUTTON = (By.ID, "menu-item-27617")
    PRACTICE_SITE_1_BUTTON = (By.ID, "menu-item-27618")

    #тест-кейс 4
    YOUTUBE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="YouTube"]')

    #тест-кейс 5
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    USERNAME_DESCRIPTION_INPUT = (By.ID, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn btn-danger")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "p.ng-scope")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    #тест-кейс 6
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger")
