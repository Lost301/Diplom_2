import allure
import requests

import data


class StellarBurgersApi:

    @staticmethod
    @allure.step('Создать пользователя')
    def create_user(body):
        return requests.post(data.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Выполнить логин пользователя')
    def login_user(email, password):
        return requests.post(data.LOGIN_USER, json={'email': email, 'password': password})

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(data.DELETE_USER, headers=headers)

    @staticmethod
    @allure.step('Получить список ингредиентов')
    def get_ingredients():
        return requests.get(data.GET_INGREDIENTS)

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(ingredients, token=None):
        headers = {'Authorization': token} if token else {}
        return requests.post(data.CREATE_ORDER, json={'ingredients': ingredients}, headers=headers)
