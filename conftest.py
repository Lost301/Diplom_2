import pytest

from helpers import generate_user_body
from stellar_burgers_api import StellarBurgersApi


@pytest.fixture
def registered_user():
    body = generate_user_body()
    response = StellarBurgersApi.create_user(body)
    token = response.json().get('accessToken', '')
    yield body, token
    StellarBurgersApi.delete_user(token)


@pytest.fixture
def ingredient_ids():
    response = StellarBurgersApi.get_ingredients()
    ingredients = response.json()['data']
    bun = next(item['_id'] for item in ingredients if item['type'] == 'bun')
    main = next(item['_id'] for item in ingredients if item['type'] == 'main')
    return [bun, main]
