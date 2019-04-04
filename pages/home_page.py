from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self):
        self.driver.get(self.get_url())
        return HomePage(self.driver)

    """
    Locators, __init__ and other methods
    """
    _url =""

    def get_url(self):
        return super()._url+ self._url

    def __init__(self, driver):
        super().__init__(driver)