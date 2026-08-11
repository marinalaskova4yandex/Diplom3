import allure
import time
from pages.base_page import BasePage
from locators.main_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Перейти в Ленту заказов")
    def go_to_order_feed(self):
        self.click_element(MainPageLocators.ORDER_FEED_TAB)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self):
        self.click_element(MainPageLocators.CONSTRUCTOR_TAB)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT_CARD)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    @allure.step("Добавить ингредиент в заказ через Drag and Drop")
    def add_ingredient_to_burger(self):
        source = self.wait_for_visibility(MainPageLocators.INGREDIENT_CARD)
        target = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_ZONE)

        # Скроллим к элементу перед переносом
        self.driver.execute_script("arguments[0].scrollIntoView(true);", source)
        time.sleep(0.3)

        # Выполняем стабильный JS Drag and Drop для полной кроссбраузерности
        js_drag_drop = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function (key, value) { this.data[key] = value; },
                getData: function (key) { return this.data[key]; }
            };
            return event;
        }
        function dispatchEvent(element, eventType, event) {
            if (element.dispatchEvent) { element.dispatchEvent(event); }
        }
        var sourceEle = arguments[0];
        var targetEle = arguments[1];
        var dragStartEvent = createEvent('dragstart');
        dispatchEvent(sourceEle, 'dragstart', dragStartEvent);
        var dragEnterEvent = createEvent('dragenter');
        dispatchEvent(targetEle, 'dragenter', dragEnterEvent);
        var dragOverEvent = createEvent('dragover');
        dispatchEvent(targetEle, 'dragover', dragOverEvent);
        var dropEvent = createEvent('drop');
        dropEvent.dataTransfer = dragStartEvent.dataTransfer;
        dispatchEvent(targetEle, 'drop', dropEvent);
        var dragEndEvent = createEvent('dragend');
        dispatchEvent(sourceEle, 'dragend', dragEndEvent);
        """
        self.driver.execute_script(js_drag_drop, source, target)
        time.sleep(0.5)

    @allure.step("Кликнуть кнопку Оформить заказ через JS")
    def click_order_button_js(self):        
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        
        button = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )        
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_count(self):
        try:
            el = self.driver.find_element(*MainPageLocators.BUN_COUNTER)
            return int(el.text) if el.text.strip() else 0
        except Exception:
            return 0