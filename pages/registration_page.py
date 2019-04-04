from pages.base_page import BasePage


class RegistrationPage(BasePage):

    _url=""

    def get_url(self):
        super()._url = self._url

    def __init__(self, driver):
        super().__init__(driver)
