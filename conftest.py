import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data_for_tests.url import Url


@pytest.fixture(name="driver")
def get_driver():
    ff_options = Options()
    ff_options.add_argument('--kiosk')  # '--kiosk' - применять для MAC и Linux, '--start-maximized' - для Windows
    driver = webdriver.Firefox(options=ff_options)
    driver.get(Url.yandex_scooter)

    yield driver

    driver.quit()
