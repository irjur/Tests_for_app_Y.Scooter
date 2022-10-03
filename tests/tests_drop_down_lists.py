import pytest
from pages.main_page import MainPageScooter
from parametrize.parametrize import DropDownLists


class TestsDropDownLists:
    @pytest.mark.parametrize('question, answer, text_answer', DropDownLists.data)
    def test_click_question(self, question, answer, text_answer, driver):
        self.driver = driver
        main_page = MainPageScooter(self.driver)

        main_page.wait_for_load_main_page()
        main_page.click_question(question)

        text = main_page.text_answer(answer)

        assert text == text_answer
