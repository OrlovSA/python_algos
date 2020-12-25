"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time()
        res = f(*args, **kwargs)
        print (f"Время выполнения функции: {round(time()-t, 3)}")
        return res
    return tmp


@timer
def list_in(num):
    result = [i for i in range(num)]
    print(len(result), type(result))


@timer
def dict_in(num):
    n = range(num)
    result = {i: x for i, x in zip(n, n)}
    print(len(result), type(result))


list_in(10000000) #0.545
dict_in(10000000) #1.375