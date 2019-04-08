from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


class PageManager:

    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.home_page = HomePage(driver)
        self.account_page = AccountPage(driver)
