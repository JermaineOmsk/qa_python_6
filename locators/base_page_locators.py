from selenium.webdriver.common.by import By
class QuestionLocators:
    q_price_and_payment = (By.ID, "accordion__heading-0")#Сколько это стоит? И как оплатить?(кликабельно,выпадающий список)
    a_price_and_payment = (By.ID, "accordion__panel-0")#Сутки — 400 рублей. Оплата курьеру — наличными или картой.
    q_how_much = (By.ID, "accordion__heading-1")#Хочу сразу несколько самокатов! Так можно?И как оплатить?(кликабельно,выпадающий список)
    a_how_much = (By.ID, "accordion__panel-1")#Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.
    q_rental_time = (By.ID, "accordion__heading-2")#Как рассчитывается время аренды?? И как оплатить?(кликабельно,выпадающий список)
    a_rental_time = (By.ID, "accordion__panel-2")#Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.
    q_order_today = (By.ID, "accordion__heading-3")#Можно ли заказать самокат прямо на сегодня?(кликабельно,выпадающий список)
    a_order_today = (By.ID, "accordion__panel-3")#Только начиная с завтрашнего дня. Но скоро станем расторопнее.
    q_extend_order_or_return = (By.ID, "accordion__heading-4")#Можно ли продлить заказ или вернуть самокат раньше?(кликабельно,выпадающий список)
    a_extend_order_or_return = (By.ID, "accordion__panel-4")#Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
    q_charger_with_scooter = (By.ID, "accordion__heading-5")#Вы привозите зарядку вместе с самокатом?(кликабельно,выпадающий список)
    a_charger_with_scooter = (By.ID, "accordion__panel-5")#Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.
    q_cancel_order = (By.ID, "accordion__heading-6")#Можно ли отменить заказ?(кликабельно,выпадающий список)
    a_cancel_order = (By.ID, "accordion__panel-6")#Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
    q_across_mkad = (By.ID, "accordion__heading-7")#Я жизу за МКАДом, привезёте?(кликабельно,выпадающий список)
    a_across_mkad = (By.ID, "accordion__panel-7")#Да, обязательно. Всем самокатов! И Москве, и Московской области.

class BasePageElements:    
    order_button_top_of_page = (By.CLASS_NAME, "Button_Button__ra12g")#кнопка заказать вверху страницы
    order_button_bottom_of_page =  (By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")#кнопка заказать внизу страницы
    logo_scooter = (By.XPATH, "//img[@alt='Scooter']")#логотип левый угол самокат
    logo_yandex = (By.XPATH, "//img[@alt='Yandex']")#логотип яндекс
    faq_area = (By.CLASS_NAME, "Home_FourPart__1uthg")#вопросы о важном
    logo_scooter_few_days =  (By.XPATH, "//div[@class='Home_Header__iJKdX']")#Самокат на пару дней
   
