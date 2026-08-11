import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from endpoints import BASE_URL

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.timeout = timeout
        self.base_url = BASE_URL

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_text_to_be_present(self, locator):        
        return WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.find_element(*locator).text.strip() != ""
        )

    @allure.step("Открыть страницу {path}")
    def navigate(self, path=""):
        target_url = f"{self.base_url.rstrip('/')}{path}"
        try:
            self.driver.get(target_url)
        except Exception:
            self.driver.refresh()

    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        self.wait_for_text_to_be_present(locator)
        return self.find_element(locator).text.strip()