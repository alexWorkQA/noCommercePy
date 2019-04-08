from selenium.webdriver.common.by import By

from web_elements.web_element import WebElement


class TextField(WebElement):

    def __init__(self, driver, selector):
        super().__init__(driver, selector)

    def clear_fld(self):
        super()._wait_element(self.selector)
        element = self.driver.find_element(By.XPATH, self.selector)
        element.clear()

    def enter_value(self, value):
        super()._wait_element(self.selector)
        element = self.driver.find_element(By.XPATH, self.selector)
        element.send_keys(value)

    def get_attribute(self):
        super()._wait_element(self.selector)
        element = self.driver.find_element(By.XPATH, self.selector)
        return element.get_attribute("value")
