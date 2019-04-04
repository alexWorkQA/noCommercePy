from pages.login_page import LoginPage


class PageManager:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
