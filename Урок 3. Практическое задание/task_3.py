"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""

from hashlib import sha256


def input_users():
    iu = input('Введите строку: ')
    return count_str(iu)


def count_str(iu):
    res = []
    for i in range(1, len(iu) + 1):
        for n in range(0, i):
            el = sha256(iu[n:i].encode()).hexdigest()
            res.append(el)
    sub_set = set(res)
    print(f'Число подстрок {iu} - {len(sub_set) - 1}')
    return input_users()


input_users()