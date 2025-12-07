import pytest
import random
import string
import requests  # <-- НОВОЕ


BASE_URL = "https://stellarburgers.education-services.ru/api"


def generate_random_email() -> str:
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"test_{suffix}@yandex.ru"


@pytest.fixture
def register_url() -> str:
    return f"{BASE_URL}/auth/register"


@pytest.fixture
def login_url() -> str:
    return f"{BASE_URL}/auth/login"


@pytest.fixture
def orders_url() -> str:
    return f"{BASE_URL}/orders"


@pytest.fixture
def ingredients_url() -> str:
    return f"{BASE_URL}/ingredients"


@pytest.fixture
def new_user_data() -> dict:
    return {
        "email": generate_random_email(),
        "password": "password123",
        "name": "Test User",
    }


@pytest.fixture
def auth_headers(register_url, new_user_data) -> dict:
    """Регистрирует нового пользователя и возвращает заголовок Authorization."""
    response = requests.post(register_url, json=new_user_data)
    assert response.status_code == 200

    body = response.json()
    access_token = body["accessToken"]  # уже в формате 'Bearer ...'
    return {"Authorization": access_token}


@pytest.fixture
def valid_ingredient_ids(ingredients_url) -> list[str]:
    """Получает список валидных id ингредиентов с сервера."""
    response = requests.get(ingredients_url)
    response.raise_for_status()

    data = response.json()
    # Берём несколько первых ингредиентов
    return [item["_id"] for item in data["data"][:3]]
