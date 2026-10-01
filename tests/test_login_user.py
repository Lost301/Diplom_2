import allure

from stellar_burgers_api import StellarBurgersApi


@allure.epic('Stellar Burgers API')
@allure.feature('Логин пользователя')
class TestLoginUser:

    @allure.title('Вход под существующим пользователем')
    def test_login_existing_user_success(self, registered_user):
        body, _, _ = registered_user
        response = StellarBurgersApi.login_user(body['email'], body['password'])

        assert response.status_code == 200
        assert response.json()['success'] is True
        assert 'accessToken' in response.json()
        assert response.json()['user']['email'] == body['email']

    @allure.title('Вход с неверным логином и паролем')
    def test_login_with_wrong_credentials_failed(self, registered_user):
        body, _, _ = registered_user
        response = StellarBurgersApi.login_user(body['email'], 'wrong_password')

        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'email or password are incorrect'}
