import allure

from pages.base_page import BasePageScooter
from locators.redirect_page_locators import RedirectPageLocators


class RedirectPage(BasePageScooter):
    @allure.step('Переход на главную страницу "Дзена"')
    def go_to_yandex_dzen(self):
        self.click_to_element(RedirectPageLocators.logo_yandex)
        self.switch_window()
        self.find_element_with_wait(RedirectPageLocators.button_to_find)
        return self.current_url_page()
