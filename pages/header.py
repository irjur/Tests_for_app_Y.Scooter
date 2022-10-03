from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Header, MainPage


class HeaderScooter:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_load_main_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(MainPage.home_page))

    def button_order_up_click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(Header.button_order_up))
        self.driver.find_element(*Header.button_order_up).click()

    def logo_yandex_click(self):
        self.wait_for_load_main_page()
        self.wait.until(expected_conditions.element_to_be_clickable(Header.logo_yandex))
        self.driver.find_element(*Header.logo_yandex).click()

    def logo_scooter_click(self):
        self.wait_for_load_main_page()
        self.button_order_up_click()
        self.wait.until(expected_conditions.element_to_be_clickable(Header.logo_scooter))
        self.driver.find_element(*Header.logo_scooter).click()
