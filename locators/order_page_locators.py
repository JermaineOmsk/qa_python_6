from selenium.webdriver.common.by import By
class OrderLocators:
    name = (By.XPATH, "//input[@placeholder='* Имя']")#поле имя
    surname = (By.XPATH, "//input[@placeholder='* Фамилия']")#поле фамилия
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")#поле адрес
    metro_station = (By.XPATH, "//input[@placeholder='* Станция метро']")#поле метро
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")#поле телефон
    button_next = (By.XPATH, "//button[text() = 'Далее']" )#кнопка далее
    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")#поле когда привезти самокат
    rental_period = (By.CLASS_NAME, 'Dropdown-placeholder' )#поле срок аренды
    rental_period_one = (By.XPATH, "//div[text()='сутки']")
    rental_period_two = (By.XPATH, "//div[text()='двое суток']")
    rental_period_three = (By.XPATH, "//div[text()='трое суток']")
    rental_period_four = (By.XPATH, "//div[text()='четверо суток']")
    rental_period_five = (By.XPATH, "//div[text()='пятеро суток']")
    rental_period_six = (By.XPATH, "//div[text()='шестеро суток']")
    rental_period_seven = (By.XPATH, "//div[text()='семеро суток']")
    check_box_black = (By.ID, "black")#чекбокс цвет самоката черный жемчуг
    check_box_grey = (By.ID,  "grey")#чекбокс цвет самоката серая безысходность
    order_button_middle =  (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")#кнопка заказать после заполнения всех полей 
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    text_would_you_like_to_place_an_order = (By.XPATH, "//div[text()='Хотите оформить заказ?']")#хотите оформить заказ?
    button_confirm_order_yes = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")#кнопка подтверждения заказа ДА
    order_confirm_text = (By.XPATH, "//div[text()='Заказ оформлен']")#надпись заказ оформел
    button_view_status = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Посмотреть статус']")
    number_of_order = (By.XPATH, "//div[contains(text(), 'Номер заказа:')]")#номер заказа при оформлении заказа
    number_of_order_view_status = (By.CLASS_NAME, "Input_Input__1iN_Z Track_Input__1g7lq Input_Filled__1rDxs Input_Responsible__1jDKN")#просмотр статуса заказа по номеру
    text_who_is_the_scooter_for = (By.XPATH, "//div[contains(text(), 'Для кого самокат')]")