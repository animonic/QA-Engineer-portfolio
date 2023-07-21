# Елена Платонова, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request


# Функция для позитивной проверки
def positive_assert_200(track):
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
    print(sender_stand_request.track)


# Тест 1. Запрос с существующим трекером
def test_get_order_by_track_success_response():
    positive_assert_200(sender_stand_request.track)
    print(sender_stand_request.track)
