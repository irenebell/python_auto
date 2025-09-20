import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(optionsgit=options)
    driver.maximize_window()
    driver.implicitly_wait(3)
    yield driver
    driver.close()