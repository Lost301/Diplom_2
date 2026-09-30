import allure

from helpers import generate_user_body
from stellar_burgers_api import StellarBurgersApi


@allure.epic('Stellar Burgers API')
@allure.feature('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user_success(self):
        body = generate_user_body()
        response = StellarBurgersApi.create_user(body)
        token = response.json().get('accessToken', '')

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert response.json()['user']['email'] == body['email']

        StellarBurgersApi.delete_user(token)

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_existing_user_failed(self, registered_user):
        body, _ = registered_user
        response = StellarBurgersApi.create_user(body)

        assert response.status_code == 403
        assert response.json() == {'success': False, 'message': 'User already exists'}

    @allure.title('Создание пользователя без обязательного поля')
    def test_create_user_without_required_field_failed(self):
        body = generate_user_body()
        del body['name']
        response = StellarBurgersApi.create_user(body)

        assert response.status_code == 403
        assert response.json() == {
            'success': False,
            'message': 'Email, password and name are required fields'
        }
