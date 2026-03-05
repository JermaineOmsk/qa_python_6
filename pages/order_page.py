import pytest
import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators
from selenium.webdriver.common.keys import Keys
class OrderPage(BasePage):
    @allure.step('Открываем форму заказа')
    def open_order_page(self, locator):
        self.click(locator)
        self.wait_for_visibility(OrderLocators.text_who_is_the_scooter_for)
    @allure.step('Заполняем поля формы заказа')
    def fill_in_the_order_fields(self, user_name, user_surname, user_address,  user_metro_station, user_phone, user_date, rental_time, check_box):
        self.find(OrderLocators.name).send_keys(user_name)
        self.find(OrderLocators.surname).send_keys(user_surname)
        self.find(OrderLocators.address).send_keys(user_address)
        self.find(OrderLocators.metro_station).send_keys(user_metro_station, Keys.DOWN, Keys.ENTER)
        self.find(OrderLocators.phone).send_keys(user_phone)
        self.click(OrderLocators.button_next)
        self.find(OrderLocators.date).send_keys(user_date, Keys.ENTER)
        self.click(OrderLocators.rental_period)
        self.click(rental_time)
        self.click(check_box)
        self.find(OrderLocators.comment).send_keys('Вези быстрее')
        self.click(OrderLocators.order_button_middle)
        self.wait_for_visibility(OrderLocators.text_would_you_like_to_place_an_order)
        self.click(OrderLocators.button_confirm_order_yes)
        