"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
from hashlib import sha256
from uuid import uuid4


def gen_hex():
    user_password = input('Введите пароль: ')
    salt = uuid4().hex
    return validation_hex(salt, user_password)


def validation_hex(salt, paswd):
    pas_hex_1 = sha256(salt.encode() + paswd.encode('utf-8')).hexdigest()
    print(pas_hex_1)
    user_password = input('Введите повторно пароль: ')
    pas_hex_2 = sha256(salt.encode() + user_password.encode('utf-8')).hexdigest()
    print(pas_hex_2)
    if pas_hex_1 == pas_hex_2:
        print('Пароли совподают')
    else:
        print('Пароли НЕ совподают')


gen_hex()