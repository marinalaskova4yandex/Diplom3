import allure
import requests
from endpoints import ORDERS

class OrderApiHelper:
    @staticmethod
    def create_order(token, ingredient_ids):
        """Создает заказ через API для переданного пользователя."""
        headers = {"Authorization": token}
        payload = {"ingredients": ingredient_ids}
        
        with allure.step("Создание заказа через API"):
            return requests.post(ORDERS, json=payload, headers=headers)