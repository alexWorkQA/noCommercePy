from pages.base_page import BasePage
from web_elements.text_field import TextField


class AccountPage(BasePage):

    def get_first_name(self):
        return self.first_name_fld.get_attribute()

    def get_last_name(self):
        return self.last_name_fld.get_attribute()

    def get_email(self):
        return self.email_fld.get_attribute()

    _url = "customer/info"
    _first_name_fld = ".//input[@id='FirstName']"
    _last_name_fld = ".//input[@id='LastName']"
    _email_fld = ".//input[@id='Email']"

    def _get_url(self):
        return super()._url + self._url

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_fld = TextField(driver, self._first_name_fld)
        self.last_name_fld = TextField(driver, self._last_name_fld)
        self.email_fld = TextField(driver, self._email_fld)
