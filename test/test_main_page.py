import allure
import pytest

from data import ANSWER_TEXTS
from pages.main_page import MainPageScooter
from conftest import driver


class TestQuestionImportant:
    @pytest.mark.parametrize(
        'number, expected_text',
        [
            (0, ANSWER_TEXTS[0]),
            (1, ANSWER_TEXTS[1]),
            (2, ANSWER_TEXTS[2]),
            (3, ANSWER_TEXTS[3]),
            (4, ANSWER_TEXTS[4]),
            (5, ANSWER_TEXTS[5]),
            (6, ANSWER_TEXTS[6]),
            (7, ANSWER_TEXTS[7])
        ]
    )
    @allure.title('Проверка ответа на соответсвующий текст')
    @allure.description('На главной странице проверяем, что текст ответа соответсвующий вопросу')
    def test_answer_and_question(self, driver, number, expected_text):
        driver.get("https://qa-scooter.praktikum-services.ru/")

        main_page = MainPageScooter(driver)
        assert main_page.check_answer_question(number) == expected_text
