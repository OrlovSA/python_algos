"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

from hashlib import sha256
from uuid import uuid4


class hex_url():
    def __init__(self):
        self.salt_url = {}
        self.salt = uuid4().hex

    def input_url(self):
        url = input('Введите URL: ')
        return self.validate_u_s(url)

    def validate_u_s(self, url):
        if self.salt_url.get(url) == None:
            print('записи нет')
            hexurl = sha256(self.salt.encode() + url.encode('utf-8')).hexdigest()
            self.salt_url.update({url: hexurl})
            print(f'Запись создана\n{self.salt_url.get(url)}')
        else:
            print(f'Запись существует\n{self.salt_url.get(url)}')
        return self.input_url()


if __name__ == "__main__":
    hu = hex_url()
    hu.input_url()