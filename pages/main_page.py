import pytest
import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators
from locators.base_page_locators import BasePageElements
from selenium.webdriver.common.keys import Keys
from urls import dzen_url
class MainPage(BasePage,):

    def find_faq_area(self):
        return self.find(BasePageElements.faq_area)

    def click_button_top(self):
        self.click(BasePageElements.order_button_top_of_page)
        
    def wait_for_order_page(self):    
        return self.wait_for_visibility(OrderLocators.text_who_is_the_scooter_for)

    def find_button_bottom(self):
        return self.find(BasePageElements.order_button_bottom_of_page)

    def click_button_bottom(self):
        self.click(BasePageElements.order_button_bottom_of_page)    

    def click_logo_scooter(self):
        self.click(BasePageElements.logo_scooter)  

    def wait_for_logo_scooter_few_days(self):    
        return self.wait_for_visibility(BasePageElements.logo_scooter_few_days)    

    def click_logo_yandex(self):
        self.click(BasePageElements.logo_yandex)

    def wait_for_url_dzen(self):
        return self.wait_for_url(dzen_url)