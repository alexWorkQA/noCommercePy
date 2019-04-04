from pages.base_page import BasePage
from web_elements.button import Button
from web_elements.text_field import TextField


class LoginPage(BasePage):

    def click_login_btn(self):
        """
        @type: Click login btn <params>
        """
        self.lgn_btn.click()
        return LoginPage(self.driver)

    def enter_email(self, _):
        self.email_fld.clear_fld()
        self.email_fld.enter_value(_)
        return LoginPage(self.driver)

    def enter_pass(self, _):
        self.pass_fld.clear_fld()
        self.pass_fld.enter_value(_)
        return LoginPage(self.driver)

    def open(self):
        self.driver.get(self.get_url())
        return LoginPage(self.driver)

    """Locators, __init__ and other methods"""
    _url = "/login"
    _login_btn = ".//input[@class='button-1 login-button']"
    _email_fld = ".//input[@id='Email']"
    _pass_fld = ".//input[@id='Password']"

    def get_url(self):
        return super()._url + self._url

    def __init__(self, driver):
        super().__init__(driver)
        self.lgn_btn = Button(driver, self._login_btn)
        self.email_fld = TextField(driver, self._email_fld)
        self.pass_fld = TextField(driver, self._pass_fld)
