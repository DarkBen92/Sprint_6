from selenium.webdriver.common.by import By


class OrderPageLocators:
    input_name = By.XPATH, "//input[@placeholder = '* Имя']"
    input_surname = By.XPATH, "//input[@placeholder = '* Фамилия']"
    input_address = By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"
    input_metro_station = By.XPATH, "//input[@placeholder = '* Станция метро']"
    button_select_metro_station = By.XPATH, "//button[@value = '{}']"
    input_phone_number = By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"
    order_next_button = By.XPATH, "//div[@class = 'Order_NextButton__1_rCA']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    input_time = By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"
    input_period = By.XPATH, "//span[@class = 'Dropdown-arrow']"
    select_period = By.XPATH, "//div[@class = 'Dropdown-option'][{}]"
    checkbox_color = By.XPATH, "//input[@id = '{}']"
    input_comment = By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"
    order_button = By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    button_yes = By.XPATH, "//div[@class = 'Order_Modal__YZ-d3']//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']"
    text_success_order = By.XPATH, "//div[@class ='Order_Text__2broi']/parent::div[@class ='Order_ModalHeader__3FDaJ']"
    logo_scooter = By.XPATH, "//a[@class = 'Header_LogoScooter__3lsAR']"
