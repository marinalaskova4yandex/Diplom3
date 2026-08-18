import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.main_locators import FeedPageLocators

class FeedPage(BasePage):

    @allure.step("Получить количество выполненных заказов за все время")
    def get_all_time_orders(self):        
        return int(self.get_text(FeedPageLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders(self):
        return int(self.get_text(FeedPageLocators.TODAY_ORDERS_COUNTER))

    @allure.step("Проверить, появился ли любой номер заказа на доске 'В работе'")
    def is_any_order_in_progress(self):         
        self.wait_for_visibility(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        for el in elements:
            text_val = el.text.strip() 
            if text_val.isdigit():
                return True
        return False

    @allure.step("Ожидать увеличения счетчика заказов 'за все время'")
    def wait_for_all_time_orders_increase(self, old_count):        
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: self.get_all_time_orders() > old_count
        )

    @allure.step("Ожидать увеличения счетчика заказов 'за сегодня'")
    def wait_for_today_orders_increase(self, old_count):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: self.get_today_orders() > old_count
        )

    @allure.step("Ожидать появления любого заказа в статусе 'В работе'")
    def wait_for_order_to_appear_in_progress(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: self.is_any_order_in_progress()
        )