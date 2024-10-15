import allure

from pages.base_page import BasePageScooter
from locators.order_page_locators import OrderPageLocators


class OrderPageScooter(BasePageScooter):
    @allure.step('Оформление заказа')
    def set_order(
            self, name, surname, address, number, phone_number, time, color, comment
    ):
        self.add_text_to_element(OrderPageLocators.input_name, name)
        self.add_text_to_element(OrderPageLocators.input_surname, surname)
        self.add_text_to_element(OrderPageLocators.input_address, address)
        self.click_to_element(OrderPageLocators.input_metro_station)
        station_metro = self.set_locator(OrderPageLocators.button_select_metro_station, number)
        self.click_to_element(station_metro)
        self.add_text_to_element(OrderPageLocators.input_phone_number, phone_number)
        self.click_to_element(OrderPageLocators.order_next_button)
        self.add_text_to_element(OrderPageLocators.input_time, time)
        self.click_to_element(OrderPageLocators.input_period)
        period = self.set_locator(OrderPageLocators.select_period, number)
        self.click_to_element(period)
        colors = self.set_locator(OrderPageLocators.checkbox_color, color)
        self.click_to_element(colors)
        self.add_text_to_element(OrderPageLocators.input_comment, comment)
        self.click_to_element(OrderPageLocators.order_button)
        self.click_to_element(OrderPageLocators.button_yes)

    @allure.step('Проверка успешного заказа')
    def check_success_order(self):
        return self.text_from_element(OrderPageLocators.text_success_order)

    @allure.step('Переход на главную страницу "Самоката"')
    def go_to_main_page(self):
        self.click_to_element(OrderPageLocators.order_next_button)
        self.click_to_element(OrderPageLocators.logo_scooter)
        return self.current_url_page()
