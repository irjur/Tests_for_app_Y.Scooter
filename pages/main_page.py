from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPage


class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def wait_for_load_main_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(MainPage.home_page))

    def click_question(self, question):
        self.wait.until(expected_conditions.visibility_of_element_located(question))
        element = self.driver.find_element(*question)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        self.wait.until(expected_conditions.visibility_of_element_located(question))
        self.wait.until(expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    def text_answer(self, answer):
        return self.driver.find_element(*answer).text
