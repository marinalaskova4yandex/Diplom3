import allure
from locators.main_locators import MainPageLocators

@allure.suite("Основная функциональность - Ингредиенты")
class TestIngredientModal:

    @allure.title("Появление всплывающего окна с деталями при клике на ингредиент")
    def test_open_ingredient_modal(self, main_page):
        main_page.navigate()
        main_page.click_first_ingredient()
        assert main_page.wait_for_visibility(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_close_ingredient_modal(self, main_page):
        main_page.navigate()
        main_page.click_first_ingredient()
        main_page.close_modal()
        assert main_page.wait_for_invisibility(MainPageLocators.INGREDIENT_MODAL)

    @allure.title("Увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases(self, main_page):
        main_page.navigate()
        initial_count = main_page.get_ingredient_count()
        main_page.add_ingredient_to_burger()
        new_count = main_page.get_ingredient_count()
        assert new_count > initial_count