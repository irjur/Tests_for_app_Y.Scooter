from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RentPage, MainPage, Header


class RentPageScooter:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_for_load_main_page(self):
        self.wait.until(expected_conditions.visibility_of_element_located(MainPage.home_page))

    def button_order_up_click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(Header.button_order_up))
        self.driver.find_element(*Header.button_order_up).click()

    def button_order_down_click(self):
        element = self.driver.find_element(*MainPage.button_order_down)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
        self.wait.until(expected_conditions.element_to_be_clickable(MainPage.button_order_down))
        self.driver.find_element(*MainPage.button_order_down).click()

    def wait_for_load_for_whole_scooter_form(self):
        self.wait.until(expected_conditions.visibility_of_element_located(RentPage.header_for_whole_scooter))

    def enter_name(self, name):
        self.driver.find_element(*RentPage.input_name).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*RentPage.input_surname).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*RentPage.input_address).send_keys(address)

    def enter_metro_station(self, metro_station):
        self.driver.find_element(*RentPage.input_metro_station).send_keys(metro_station)
        self.wait.until(expected_conditions.element_to_be_clickable(RentPage.drop_down_metro_station))
        self.driver.find_element(*RentPage.select_metro_station).click()

    def enter_phone(self, phone):
        self.driver.find_element(*RentPage.input_phone).send_keys(phone)

    def button_onward_click(self):
        self.wait.until(expected_conditions.element_to_be_clickable(RentPage.button_onward))
        self.driver.find_element(*RentPage.button_onward).click()

    def wait_for_load_about_rent_form(self):
        self.wait.until(expected_conditions.visibility_of_element_located(RentPage.header_about_rent))

    def enter_data(self, data):
        self.driver.find_element(*RentPage.input_data).send_keys(data)
        self.wait.until(expected_conditions.element_to_be_clickable(RentPage.date_selected))
        self.driver.find_element(*RentPage.date_selected).click()

    def enter_rental_period(self, period):
        self.driver.find_element(*RentPage.input_rental_period).click()
        self.wait.until(expected_conditions.element_to_be_clickable(RentPage.drop_down_rental_period))
        self.driver.find_element(By.XPATH, f'//div[contains(text(), "{period}")]').click()

    def choose_color(self, color):
        self.driver.find_element(By.ID, color).click()

    def enter_comment(self, comment):
        self.driver.find_element(*RentPage.input_comment).send_keys(comment)

    def button_order_click(self):
        self.driver.find_element(*RentPage.button_order).click()

    def wait_for_load_pop_up_confirm(self):
        self.wait.until(expected_conditions.visibility_of_element_located(RentPage.pop_up_confirm))

    def button_yes_click(self):
        self.driver.find_element(*RentPage.button_yes).click()

    def wait_for_load_pop_up_order_processed(self):
        self.wait.until(expected_conditions.visibility_of_element_located(RentPage.pop_up_order_processed))
        return self.driver.find_element(*RentPage.button_view_status).text

    def fill_for_whole_scooter_form(self, name, surname, address, metro_station, phone):
        self.wait_for_load_for_whole_scooter_form()
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_address(address)
        self.enter_metro_station(metro_station)
        self.enter_phone(phone)
        self.button_onward_click()

    def fill_about_rent_form(self, data, period, color, comment):
        self.wait_for_load_about_rent_form()
        self.enter_data(data)
        self.enter_rental_period(period)
        self.choose_color(color)
        self.enter_comment(comment)
        self.button_order_click()
        self.wait_for_load_pop_up_confirm()
        self.button_yes_click()
