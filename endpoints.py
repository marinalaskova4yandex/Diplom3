BASE_URL = "https://stellarburgers.education-services.ru/"

# Эндпоинты пользователя
CREATE_USER = f"{BASE_URL}api/auth/register"
LOGIN_USER = f"{BASE_URL}api/auth/login"
USER_DATA = f"{BASE_URL}api/auth/user"  # Используется для удаления в фикстурах

# Эндпоинты заказов и ингредиентов
ORDERS = f"{BASE_URL}api/orders"
INGREDIENTS = f"{BASE_URL}api/ingredients"