import allure

from stellar_burgers_api import StellarBurgersApi


@allure.epic('Stellar Burgers API')
@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth_success(self, registered_user, ingredient_ids):
        _, token = registered_user
        response = StellarBurgersApi.create_order(ingredient_ids, token)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'number' in response.json()['order']
        assert 'name' in response.json()

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth_success(self, ingredient_ids):
        response = StellarBurgersApi.create_order(ingredient_ids)

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'number' in response.json()['order']

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients_failed(self, registered_user):
        _, token = registered_user
        response = StellarBurgersApi.create_order([], token)

        assert response.status_code == 400
        assert response.json() == {
            'success': False,
            'message': 'Ingredient ids must be provided'
        }

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_with_invalid_ingredient_hash_failed(self, registered_user):
        _, token = registered_user
        response = StellarBurgersApi.create_order(['invalid_hash_12345'], token)

        assert response.status_code == 500
