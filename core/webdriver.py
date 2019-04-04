from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_webdriver():
    return webdriver.Chrome(ChromeDriverManager().install())
