from pages.rent_page import RentPageScooter
import data_for_tests.Bilbo_Baggins as Bilbo_Baggins
import data_for_tests.Smaug as Smaug


class TestsOrderScooter:

    def test_order_scooter_by_button_up(self, driver):
        self.driver = driver
        rent_page = RentPageScooter(self.driver)

        rent_page.wait_for_load_main_page()
        rent_page.button_order_up_click()

        rent_page.fill_for_whole_scooter_form(Bilbo_Baggins.name, Bilbo_Baggins.surname, Bilbo_Baggins.address,
                                              Bilbo_Baggins.metro_station, Bilbo_Baggins.phone)

        rent_page.fill_about_rent_form(Bilbo_Baggins.data, Bilbo_Baggins.period,
                                       Bilbo_Baggins.color, Bilbo_Baggins.comment)

        text = rent_page.wait_for_load_pop_up_order_processed()

        assert text == 'Посмотреть статус'

    def test_order_scooter_by_button_down(self, driver):
        self.driver = driver
        rent_page = RentPageScooter(self.driver)

        rent_page.wait_for_load_main_page()
        rent_page.button_order_down_click()

        rent_page.fill_for_whole_scooter_form(Smaug.name, Smaug.surname,
                                              Smaug.address, Smaug.metro_station, Smaug.phone)

        rent_page.fill_about_rent_form(Smaug.data, Smaug.period, Smaug.color, Smaug.comment)

        text = rent_page.wait_for_load_pop_up_order_processed()

        assert text == 'Посмотреть статус'
