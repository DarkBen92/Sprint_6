from selenium.webdriver.common.by import By


class MainPageLocators:
    locators_question = By.XPATH, "//div[@ID = 'accordion__heading-{}']"
    locators_answer = By.XPATH, "//div[@ID = 'accordion__panel-{}']"
    last_question = By.XPATH, "//div[@ID = 'accordion__heading-7']"
    cookie_button = By.XPATH, "//button[@class = 'App_CookieButton__3cvqF']"
    order_button_in_header = By.XPATH, "//div[@class = 'Header_Nav__AGCXC']/button[@class = 'Button_Button__ra12g']"
    order_button_middle = By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
