import pytest
import allure
from locators.base_page_locators import QuestionLocators
from pages.base_page import BasePage
from locators.base_page_locators import BasePageElements
import time
class TestFAQ:
    @pytest.mark.parametrize("question, answer", [
    (QuestionLocators.q_price_and_payment, QuestionLocators.a_price_and_payment),
    (QuestionLocators.q_how_much, QuestionLocators.a_how_much),
    (QuestionLocators.q_rental_time, QuestionLocators.a_rental_time),
    (QuestionLocators.q_order_today, QuestionLocators.a_order_today),
    (QuestionLocators.q_extend_order_or_return, QuestionLocators.a_extend_order_or_return),
    (QuestionLocators.q_charger_with_scooter, QuestionLocators.a_charger_with_scooter),
    (QuestionLocators.q_cancel_order, QuestionLocators.a_cancel_order),
    (QuestionLocators.q_across_mkad, QuestionLocators.a_across_mkad)])
    @allure.title('Параметризированный тест, проверяет наличие ответа на вопросы о важном')
    def test_faq(self, question, answer, driver_firefox):
        faq = BasePage(driver_firefox)
        faq_area = faq.find(BasePageElements.faq_area)
        faq.scroll(faq_area)
        time.sleep(1)# да,знаю, что так делать не есть хорошо
        #но через явное ожидание тесты фейлятся,притом каждый раз разные
        #много разных вариантов перепробовал,только этот работает четко и стабильно
        faq.click(question)
        answer_element = faq.wait_for_visibility(answer)
        assert answer_element.is_displayed()