"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


num_100 = [i for i in range(1000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """Убрал Len, добавил подсчет итерируемых объектов"""
    return [num for num, i in enumerate(nums) if i % 2 == 0]


print(timeit("func_1(num_100)",
             setup="from __main__ import func_1, num_100",
             number=1000)) # 0.1198792
print(timeit("func_2(num_100)",
             setup="from __main__ import func_2, num_100",
             number=1000)) # 0.07125669999999998