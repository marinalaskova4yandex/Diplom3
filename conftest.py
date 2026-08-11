import pytest
import requests
import random
import string
from endpoints import CREATE_USER, USER_DATA
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.main_page import MainPage
from pages.feed_page import FeedPage

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@pytest.fixture
def user_data():
    """Генерирует случайные валидные данные пользователя."""
    email = f"test_{random_string()}@yandex.ru"
    password = random_string(8)
    name = f"User_{random_string(4)}"
    return {"email": email, "password": password, "name": name}

@pytest.fixture
def created_user(user_data):
    """Фикстура регистрирует пользователя и автоматически удаляет его после теста."""
    payload = user_data
    response = requests.post(CREATE_USER, json=payload)
    token = response.json().get("accessToken")
    yield payload, token
    if token:
        headers = {"Authorization": token}
        requests.delete(USER_DATA, headers=headers)

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    """Параметризованный драйвер. Автоматически запускает тесты в обоих браузерах."""
    driver = None
    
    if request.param == "chrome":
        options = webdriver.ChromeOptions()        
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")        
        driver = webdriver.Chrome(options=options)
            
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()       
        options.add_argument("--disable-gpu")        
        driver = webdriver.Firefox(options=options)
            
    if driver:
        driver.set_window_size(1920, 1080)
        yield driver
        driver.quit()
            
    
@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)