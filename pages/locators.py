from selenium.webdriver.common.by import By


class Locators:

    HEADER = (By.CSS_SELECTOR, ".ast-above-header-bar")
    HORIZONTAL_MENU = (By.ID, "ast-hf-menu-1")
    CERTIFICATION_BLOCK = (By.CSS_SELECTOR, ".elementor-element-5b4952c1")
    COURSES_BUTTON = (By.CSS_SELECTOR, ".swiper-button-next-c50f9f0")
    FOOTER = (By.CSS_SELECTOR, ".elementor-element-4cfa36e1")

    BLOCK_OF_COURSES = (By.ID, "166618a")
    FIRST_SLIDE = (By.CSS_SELECTOR, "[data-id='c50f9f0'] .swiper-slide:first-child")
    FIRST_SLIDE_TITLE = (By.CSS_SELECTOR, "[data-id='c50f9f0'] .swiper-slide:first-child .pp-info-box-title")
    SLIDER_NEXT_BUTTON = (By.CSS_SELECTOR, ".swiper-button-next-c50f9f0")

    BANNER = (By.CSS_SELECTOR, "[data-elementor-id='26600']")
    BANNER_CLOSE_BUTTON = (By.CSS_SELECTOR, ".dialog-close-button")

    SITE_NAVIGATION = (By.ID, "site-navigation")

    RESOURCES_BUTTON = (By.ID, "menu-item-27617")
    PRACTICE_SITE_1_BUTTON = (By.ID, "menu-item-27618")

    YOUTUBE_BUTTON = (By.CSS_SELECTOR, 'a[aria-label="YouTube"]')

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    USERNAME_DESCRIPTION_INPUT = (By.ID, "formly_1_input_username_0")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-danger")
    SUCCESS_MESSAGE = (By.XPATH, "//p[text()=\"You're logged in!!\"]")
    LOGOUT_LINK = (By.XPATH, "//a[text()='Logout']")

    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-danger")

    SQL_LOGIN = (By.NAME, "login")
    SQL_PASSWORD = (By.NAME, "psw")
    SQL_ENTER_BUTTON = (By.NAME, "subm1")

    MEMBER_LOGIN_BUTTON = (By.ID, "menu-item-27625")
    EMAIL_INPUT = (By.ID, "email")
