import pytest

from core.page_manager import PageManager
from core.webdriver import get_webdriver
from models.user import User


@pytest.yield_fixture()
def pm():
    driver = get_webdriver()
    driver.fullscreen_window()
    page_manager = PageManager(driver)
    yield page_manager
    driver.quit()


@pytest.yield_fixture()
def user():
    usr = User()
    usr.set_email("alex.workqa+1@gmail.com")
    usr.set_password("12345678")
    yield usr
