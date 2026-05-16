import pytest
from selenium import webdriver
from urls import scooter_url
@pytest.fixture
def driver_firefox():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(scooter_url)
    yield driver 
    driver.quit()

 