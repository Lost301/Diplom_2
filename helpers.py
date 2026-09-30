import uuid


def generate_user_body():
    return {
        'email': f'{uuid.uuid4().hex[:10]}@yandex.ru',
        'password': uuid.uuid4().hex[:12],
        'name': f'user_{uuid.uuid4().hex[:8]}'
    }
