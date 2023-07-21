# Елена Платонова, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data


# Функция для создания нового заказа
def create_new_order(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers
                         )


response = create_new_order(data.order_body)
print(response.status_code)
print(response.json())
# Функция для сохранения трек-номера
track = response.json()["track"]
print(track)


# Функция для получения заказа по трекеру
def get_order_by_track(track):
    return requests.get(configuration.BASE_URL + configuration.GET_ORDER,
                        params={'t': track})


response = get_order_by_track(track)
print(response.status_code)
print(response.json())
