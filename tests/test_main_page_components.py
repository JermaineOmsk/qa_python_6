import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from locators.base_page_locators import BasePageElements
from locators.order_page_locators import OrderLocators

class TestMainPageComponents:
    @allure.title('Проверка перехода к форме оформелия заказа через кнопку Заказать в верхней части страницы')
    def test_button_order_top_of_page(self,driver_firefox):
        button_top = BasePage(driver_firefox)
        button_top.click(BasePageElements.order_button_top_of_page)
        confirm = button_top.wait_for_visibility(OrderLocators.text_who_is_the_scooter_for)
        assert  confirm.is_displayed()
    @allure.title('Проверка перехода к форме оформелия заказа через кнопку Заказать в нижней части страницы')
    def test_button_order_bottom_of_page(self,driver_firefox):
        button_bottom = BasePage(driver_firefox)
        element = button_bottom.find(BasePageElements.order_button_bottom_of_page)
        button_bottom.scroll(element)
        button_bottom.click(BasePageElements.order_button_bottom_of_page)
        confirm = button_bottom.wait_for_visibility(OrderLocators.text_who_is_the_scooter_for)
        assert  confirm.is_displayed()    
    @allure.title('Проверка перехода на главную страницу по лкику на логотип "Самокат" ')
    def test_logo_scooter(self, driver_firefox):
        logo_scooter = BasePage(driver_firefox)
        logo_scooter.click(BasePageElements.order_button_top_of_page)    
        logo_scooter.click(BasePageElements.logo_scooter)  
        confirm = logo_scooter.wait_for_visibility(BasePageElements.logo_scooter_few_days)
        assert  confirm.is_displayed() 
    @allure.title('Проверка перехода на главную страницу "Дзен" по лкику на логотип "Яндекс" ')
    def test_logo_yandex(self, driver_firefox):
        logo_yandex = BasePage(driver_firefox)
        logo_yandex.click(BasePageElements.logo_yandex)
        windows = driver_firefox.window_handles
        if len(windows) > 1:
            driver_firefox.switch_to.window(windows[1])
      
        WebDriverWait(driver_firefox, 10).until(expected_conditions.url_to_be("https://dzen.ru/?yredirect=true"))
        assert driver_firefox.current_url == "https://dzen.ru/?yredirect=true"