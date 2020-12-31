"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
Если у вас есть идеи, предложите вариант оптимизации.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000)) # 0.0343806
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000)) # 0.03722250000000002
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000)) # 0.05607019999999999


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000)) # 0.002716100000000027
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000)) # 0.0026861999999999997
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000)) # 0.0029566000000000037


def my_version(number):
    """Не придумал как улучшить код но, было интересно сколько затратит это решение
    оно явно быстрее чем рекурсия без мемоизации"""
    i = -1
    number = str(number)
    while True:
        num = number[:i]
        if not num:
            return ''
        i -= 1


print('Моя версия my_version')
print(
    timeit(
        "my_version(num_100)",
        setup='from __main__ import my_version, num_100',
        number=10000)) # 0.010934300000000008
print(
    timeit(
        "my_version(num_1000)",
        setup='from __main__ import my_version, num_1000',
        number=10000)) # 0.013149999999999995
print(
    timeit(
        "my_version(num_10000)",
        setup='from __main__ import my_version, num_10000',
        number=10000)) # 0.01966219999999999

