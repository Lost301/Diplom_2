# Diplom_2

Автотесты для API Stellar Burgers (задание 2 диплома).

- `pytest` + `requests` + `allure-pytest`
- Тестируемые эндпоинты: создание пользователя (`/api/auth/register`), логин (`/api/auth/login`), создание заказа (`/api/orders`)

## Запуск тестов

```bash
pip install -r requirements.txt
pytest tests/ --alluredir=allure-results
```

## Отчёт Allure

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```
