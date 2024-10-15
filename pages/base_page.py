from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageScooter:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                locator))

    def current_url_page(self):
        return self.driver.current_url

    def switch_window(self):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)

    @staticmethod
    def set_locator(locator, num):
        method, locator = locator
        locator = locator.format(num)
        return method, locator
