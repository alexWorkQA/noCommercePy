from pages.base_page import BasePage
from web_elements.button import Button
from web_elements.link import Link


class HomePage(BasePage):

    def click_register_btn(self):
        self.register_btn.click()
        return HomePage(self.driver)

    def click_my_account_btn(self):
        self.my_account_btn.click()
        return HomePage(self.driver)

    def open(self):
        """

        :return:
        """
        self.driver.get(self._get_url())
        return HomePage(self.driver)

    """
    Locators, __init__ and other methods
    """
    _url = ""
    _login_btn = ".//a[@href='/login']"
    _my_account_btn = ".//a[@class='ico-account']"
    _register_btn = ".//a[@href='/register']"
    _logout_btn = ".//a[@href='/logout']"
    _computers_link = ".//a[@href='/computers']"
    _cart_link = ".//span[@class='cart-label']"

    def _get_url(self):
        return super()._url + self._url

    def __init__(self, driver):
        super().__init__(driver)
        self.login_btn = Button(driver, self._login_btn)
        self.my_account_btn = Button(driver, self._my_account_btn)
        self.register_btn = Button(driver, self._register_btn)
        self.logout_btn = Button(driver, self._logout_btn)
        self.computers_link = Link(driver, self._computers_link)
        self.cart_link = Link(driver, self._cart_link)

