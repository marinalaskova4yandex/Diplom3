import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_locators import FeedPageLocators

class FeedPage(BasePage):
    
    @allure.step("Получить количество выполненных заказов за все время")
    def get_all_time_orders(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(FeedPageLocators.TOTAL_ORDERS_COUNTER)
        )
        WebDriverWait(self.driver, self.timeout).until(lambda d: element.text.strip() != "")
        return int(element.text.strip())

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders(self):
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(FeedPageLocators.TODAY_ORDERS_COUNTER)
        )
        WebDriverWait(self.driver, self.timeout).until(lambda d: element.text.strip() != "")
        return int(element.text.strip())

    @allure.step("Проверить, появился ли любой номер заказа на доске 'В работе'")
    def is_any_order_in_progress(self):        
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        )        
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS_LIST)
        
        for el in elements:
            text_val = el.text.strip()            
            if text_val.isdigit():
                return True
                
        return False