import pytest
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageElements

class BasePage:
    def __init__(self, driver_firefox):
        self.driver_firefox = driver_firefox
    @allure.step('Поиск по локатору')
    def find(self, locator):
        return self.driver_firefox.find_element(*locator)
    @allure.step('Скрол до нужного элемента')    
    def scroll(self,element):
        self.driver_firefox.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver_firefox, 10).until(expected_conditions.visibility_of_element_located(locator))
    @allure.step('Клик по элементу')
    def click(self, locator):
        self.find(locator).click()

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver_firefox, 10).until(expected_conditions.element_to_be_clickable(locator))
        
    @allure.step('Ожидание видимости url')
    def wait_for_url(self, url):
        return WebDriverWait(self.driver_firefox, 10).until(expected_conditions.url_to_be(url))
    