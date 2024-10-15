import allure
import pytest
import pytest_check as check

from data import TEST_FIRST_ORDER, TEST_SECOND_ORDER
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from pages.redirect_page import RedirectPage
from conftest import driver


class TestOrderScooter:
    @pytest.mark.parametrize(
        'click_button, name, surname, address, number, phone_number, time, color, comment',
        [
            TEST_FIRST_ORDER,
            TEST_SECOND_ORDER
        ]
    )
    @allure.title('Проверка успешного заказа Самоката')
    @allure.description('Через кнопки "Заказать" проверяем, что заказа успешно выполнился и произошел корректный редирект')
    def test_success_order(self, driver, click_button, name, surname, address, number, phone_number, time, color, comment):
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page = MainPageScooter(driver)
        getattr(main_page, click_button)()

        order_page = OrderPageScooter(driver)
        order_page.set_order(
            name, surname, address, number, phone_number, time, color, comment
        )
        check.equal(order_page.check_success_order().split('\n')[0], "Заказ оформлен")

        check.equal(order_page.go_to_main_page(), "https://qa-scooter.praktikum-services.ru/")

        redirect_page = RedirectPage(driver)
        check.equal(redirect_page.go_to_yandex_dzen(), "https://dzen.ru/?yredirect=true")
