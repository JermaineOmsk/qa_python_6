import pytest
import allure
from locators.base_page_locators import BasePageElements
from pages.order_page import OrderPage
from locators.order_page_locators import OrderLocators
class TestOrder:

    @pytest.mark.parametrize("user_name, user_surname, user_address, user_metro_station, user_phone, user_date, rental_time, check_box", 
    [('Евгений', 'Кислицин', 'ул.Бородина 17', 'Черкизовская', '89000000000', '15.05.2026', OrderLocators.rental_period_two, OrderLocators.check_box_black), 
    ('Доздраперма', 'Октябрьская', 'Думская 100500', 'Сокольники', '89000000001', '15.05.2027', OrderLocators.rental_period_four, OrderLocators.check_box_grey)])
    @allure.title('Проверка успешного заказа самоката при вводе валидных данных ')
    def test_success_order(self,user_name, user_surname, user_address,  user_metro_station, user_phone, user_date, rental_time, check_box, driver_firefox):
        order = OrderPage(driver_firefox)
        order.open_order_page(BasePageElements.order_button_top_of_page)
        order.fill_in_the_order_fields(user_name, user_surname, user_address,  user_metro_station, user_phone, user_date, rental_time, check_box)
        confirm = order.wait_for_visibility(OrderLocators.order_confirm_text)
        assert confirm.is_displayed()
