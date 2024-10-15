import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageScooter


class MainPageScooter(BasePageScooter):
    @allure.step('Нажать на кнопку "Да все привыкли"')
    def click_cookie_button(self):
        self.click_to_element(MainPageLocators.cookie_button)

    @allure.step('Скроллить до вопроса')
    def scroll_to_questions(self):
        self.scroll_to_element(MainPageLocators.last_question)

    @allure.step('Нажать на вопрос')
    def click_on_question(self, questions_number):
        self.click_to_element(questions_number)

    @allure.step('Текст ответа')
    def get_text_answer(self, answer_number):
        return self.text_from_element(answer_number)

    @allure.step('Получить текст ответа')
    def check_answer_question(self, number):
        self.click_cookie_button()
        self.scroll_to_questions()
        questions_number = self.set_locator(MainPageLocators.locators_question, number)
        answer_number = self.set_locator(MainPageLocators.locators_answer, number)
        self.click_on_question(questions_number)
        return self.get_text_answer(answer_number)

    @allure.step('Кликнуть на кнопку "Заказать" в хэдере')
    def click_order_header_button(self):
        self.click_cookie_button()
        self.click_to_element(MainPageLocators.order_button_in_header)

    @allure.step('Кликнуть на кнопку "Заказать" в середине страницы')
    def click_order_middle_button(self):
        self.click_cookie_button()
        self.click_to_element(MainPageLocators.order_button_middle)
