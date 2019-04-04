from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Browser(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.driver.fullscreen_window()

    def click_btn(self, selector):
        self._wait_element(selector)
        element = self.driver.find_element(By.XPATH, selector)
        self._wait_element(selector)
        element.click()

    def get_txt(self, selector):
        self._wait_element(selector)
        element = self.driver.find_element(By.XPATH, selector)
        return element.text

    def _wait_element(self, selector):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, selector)))

    def clear_fld(self, selector):
        self.driver.find_element(By.XPATH, selector).clear()

    def enter_value_to_fld(self, selector, value):
        self.driver.find_element(By.XPATH, selector).send_keys(value)

    def click_back_btn(self):
        self.driver.back()

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url
