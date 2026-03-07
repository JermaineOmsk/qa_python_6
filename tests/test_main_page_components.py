import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from pages.main_page import MainPage
from locators.base_page_locators import BasePageElements
from locators.order_page_locators import OrderLocators
from urls import dzen_url

class TestMainPageComponents:
    @allure.title('Проверка перехода к форме оформелия заказа через кнопку Заказать в верхней части страницы')
    def test_button_order_top_of_page(self,driver_firefox):
        button_top = MainPage(driver_firefox)
        button_top.click_button_top()
        confirm = button_top.wait_for_order_page()
        assert  confirm.is_displayed()
    @allure.title('Проверка перехода к форме оформелия заказа через кнопку Заказать в нижней части страницы')
    def test_button_order_bottom_of_page(self,driver_firefox):
        button_bottom = MainPage(driver_firefox)
        element = button_bottom.find_button_bottom()
        button_bottom.scroll(element)
        button_bottom.click_button_bottom()
        confirm = button_bottom.wait_for_order_page()
        assert  confirm.is_displayed()    
    @allure.title('Проверка перехода на главную страницу по лкику на логотип "Самокат" ')
    def test_logo_scooter(self, driver_firefox):
        logo_scooter = MainPage(driver_firefox)
        logo_scooter.click_button_top()
        logo_scooter.click_logo_scooter()
        confirm = logo_scooter.wait_for_logo_scooter_few_days()
        assert  confirm.is_displayed() 
    @allure.title('Проверка перехода на главную страницу "Дзен" по лкику на логотип "Яндекс" ')
    def test_logo_yandex(self, driver_firefox):
        logo_yandex = MainPage(driver_firefox)
        logo_yandex.click_logo_yandex()
        windows = driver_firefox.window_handles
        if len(windows) > 1:
            driver_firefox.switch_to.window(windows[1])
      
        logo_yandex.wait_for_url_dzen()
        assert driver_firefox.current_url == dzen_url