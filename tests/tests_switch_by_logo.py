import time
from pages.header import HeaderScooter
from data_for_tests.url import Url


class TestsSwitchByLogo:

    def test_switch_by_logo_scooter(self, driver):
        self.driver = driver
        header = HeaderScooter(self.driver)

        header.logo_scooter_click()
        url = self.driver.current_url

        assert url == Url.yandex_scooter

    def test_switch_by_logo_yandex(self, driver):
        self.driver = driver
        header = HeaderScooter(self.driver)

        header.logo_yandex_click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        time.sleep(2)

        url = self.driver.current_url

        assert url == Url.yandex_search
