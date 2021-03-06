"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
from collections import Counter
from timeit import timeit


array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def my_func():
    '''По идеи должна быть самой быстрой, но почему-то в данном случае это не так
    зато самая аккуратная))'''
    result = Counter(array).most_common(1)
    return f'Чаще всего встречается число {result[0][0]}, ' \
           f'оно появилось в массиве {result[0][1]} раз(а)'


print(func_1())
print(timeit(
        'func_1()',
        setup='from __main__ import func_1',
        number=10000)) # 0.0210944

print(func_2())
print(timeit(
        'func_2()',
        setup='from __main__ import func_2',
        number=10000)) # 0.0280957

print(my_func())
print(timeit(
        'my_func()',
        setup='from __main__ import my_func',
        number=10000)) # 0.059091400000000016
