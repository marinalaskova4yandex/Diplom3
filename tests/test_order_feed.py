import allure
from helpers.helper import OrderApiHelper

@allure.suite("Раздел 'Лента заказов'")
class TestOrderFeed:

    @allure.title("Увеличение счетчика 'Выполнено за всё время' при создании заказа")
    def test_all_time_counter_increases(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user
        feed_page.navigate("/feed")
        old_count = feed_page.get_all_time_orders()
        
        # Вызов изолированного хелпера создания заказа
        OrderApiHelper.create_order(token, get_ingredient_hashes)
            
        feed_page.navigate("/feed")
        feed_page.wait_for_all_time_orders_increase(old_count)
        
        assert feed_page.get_all_time_orders() == old_count + 1

    @allure.title("Увеличение счетчика 'Выполнено за сегодня' при создании заказа")
    def test_today_counter_increases(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user
        feed_page.navigate("/feed")
        old_count = feed_page.get_today_orders()
        
        # Вызов изолированного хелпера создания заказа
        OrderApiHelper.create_order(token, get_ingredient_hashes)
            
        feed_page.navigate("/feed")
        feed_page.wait_for_today_orders_increase(old_count)
        
        assert feed_page.get_today_orders() == old_count + 1

    @allure.title("Появление номера нового заказа в разделе 'В работе'")
    def test_new_order_appears_in_progress(self, main_page, feed_page, created_user, get_ingredient_hashes):
        _, token = created_user
        
        # Вызов изолированного хелпера создания заказа
        OrderApiHelper.create_order(token, get_ingredient_hashes)
            
        feed_page.navigate("/feed")
        feed_page.wait_for_order_to_appear_in_progress()
        
        assert feed_page.is_any_order_in_progress() is True