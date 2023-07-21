import sender_stand_request
import data


# эта функция меняет значения в параметре name
def get_kit_body(name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.kit_body.copy()
    # изменение значения в поле name
    current_body["name"] = name
    # возвращается новый словарь с нужным значением name и authToken
    return current_body




# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную auth_token сохраняется токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert kit_response.json()["name"] == kit_body["name"]


# Тест 1. Успешное создание набора. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# # Тест 2. Успешное создание набора. Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Функция для негативной проверки
def negative_assert_no_name(kit_body):
    # В переменную auth_token сохраняется токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверка, что код ответа равен 400
    assert response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400


# Тест 3. Ошибка. Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body("")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)


def negative_assert_symbol(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную auth_token сохраняется токен
    auth_token = sender_stand_request.get_new_user_token(data.user_body)
    # В переменную response сохраняется результат запроса
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверка, что код ответа равен 400
    assert response.status_code == 400
    # Проверка, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400


# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора. Параметр name состоит из английских букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора. Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора. Параметр name состоит из строки спецсимволов
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора. Параметр name состоит из строки с пробелом
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("Человек и КО")


# Тест 9. Успешное создание набора. Параметр name состоит из строки с цифрами
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. В запросе нет параметра name
def test_create_kit_no_name_get_error_response():
    # Копируется словарь с телом запроса из файла data в переменную kit_body
    # Иначе можно потерять данные из исходного словаря
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)


# Тест 11. Ошибка. Тип параметра name: число
def test_create_kit_number_type_name_get_error_response():
    negative_assert_symbol(123)
