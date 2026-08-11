from selenium.webdriver.common.by import By

class HeaderLocators:
    """Локаторы кнопок в шапке сайта """
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, 'a[href="/"]')
    ORDER_FEED_BUTTON = (By.CSS_SELECTOR, 'a[href="/feed"]')


class MainPageLocators:
    """Локаторы главной страницы Конструктора """
    ORDER_FEED_TAB = (By.CSS_SELECTOR, 'a[href="/feed"]')
    CONSTRUCTOR_TAB = (By.CSS_SELECTOR, 'a[href="/"]')
    
    # Карточки ингредиентов и зона корзины конструктора
    INGREDIENT_CARD = (By.CSS_SELECTOR, '[class*="BurgerIngredient_ingredient"]')
    CONSTRUCTOR_DROP_ZONE = (By.CSS_SELECTOR, '[class*="BurgerConstructor_basket"]')
    
    # Счётчик ингредиента
    BUN_COUNTER = (By.CLASS_NAME, 'counter_counter__num__3nue1')
    
    # Модальное окно ингредиента и фоновая подложка
    INGREDIENT_MODAL = (By.CSS_SELECTOR, '[class*="Modal_modal_opened"]')
    MODAL_OVERLAY = (By.CSS_SELECTOR, '[class*="Modal_modal_overlay"]')
    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, '[class*="Modal_modal__close"]')
    
    # Кнопка оформления заказа на главной
    ORDER_BUTTON = (By.CSS_SELECTOR, "button[class*='button_button_type_primary'][class*='button_button_size_large']")


class FeedPageLocators:
    """Локаторы страницы Ленты заказов"""    
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    
    # Номера заказов внутри колонки "В работе"
    IN_PROGRESS_ORDERS_LIST = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"] li')