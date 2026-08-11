import allure
from endpoints import BASE_URL

@allure.suite("Основная функциональность - Навигация")
class TestConstructorNavigation:

    @allure.title("Переход по клику на раздел 'Лента заказов'")
    def test_navigate_to_order_feed(self, main_page, driver):
        main_page.navigate()
        main_page.go_to_order_feed()
        assert "/feed" in driver.current_url

    @allure.title("Переход по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, main_page, driver):
        main_page.navigate("/feed")
        main_page.go_to_constructor()
        assert driver.current_url == BASE_URL