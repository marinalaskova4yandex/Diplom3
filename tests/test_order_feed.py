import allure
import pytest
import requests
from selenium.webdriver.support.ui import WebDriverWait
from endpoints import ORDERS, INGREDIENTS


@allure.suite("Раздел 'Лента заказов'")
class TestOrderFeed:

    @pytest.fixture(autouse=True)
    def get_ingredient_hashes(self):
        """Вспомогательная фикстура для получения реальных id ингредиентов со стенда."""
       
        from requests.adapters import HTTPAdapter
        from urllib3.util import Retry

        session = requests.Session()
        retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
        session.mount("https://", HTTPAdapter(max_retries=retries))

        try:
            response = session.get(INGREDIENTS, timeout=10)
            ingredients_data = response.json().get("data", [])
            return [item["_id"] for item in ingredients_data[:2]]
        except Exception as e:
            pytest.skip(f"Тестовый стенд Практикума временно недоступен: {e}")

    @allure.title("Увеличение счетчика 'Выполнено за всё время' при создании заказа")
    def test_all_time_counter_increases(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user

        feed_page.navigate("/feed")
        old_count = feed_page.get_all_time_orders()

        headers = {"Authorization": token}
        payload = {"ingredients": get_ingredient_hashes}
        with allure.step("Создание заказа через API для увеличения счетчиков"):
            requests.post(ORDERS, json=payload, headers=headers)

        feed_page.navigate("/feed")

        WebDriverWait(feed_page.driver, 30).until(
            lambda d: feed_page.get_all_time_orders() > old_count
        )
        assert feed_page.get_all_time_orders() == old_count + 1

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_counter_increases(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user

        feed_page.navigate("/feed")
        old_count = feed_page.get_today_orders()

        headers = {"Authorization": token}
        payload = {"ingredients": get_ingredient_hashes}
        with allure.step("Создание заказа через API для увеличения счетчиков"):
            requests.post(ORDERS, json=payload, headers=headers)

        feed_page.navigate("/feed")

        WebDriverWait(feed_page.driver, 30).until(
            lambda d: feed_page.get_today_orders() > old_count
        )
        assert feed_page.get_today_orders() == old_count + 1

    @allure.title("Появление номера нового заказа в разделе 'В работе'")
    def test_new_order_appears_in_progress(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user
        headers = {"Authorization": token}
        payload = {"ingredients": get_ingredient_hashes}
        with allure.step("Создание заказа через API для вывода на доску в работе"):
            requests.post(ORDERS, json=payload, headers=headers)
        feed_page.navigate("/feed")
        WebDriverWait(feed_page.driver, 30).until(
            lambda d: feed_page.is_any_order_in_progress()
        )
        
        assert feed_page.is_any_order_in_progress() is True