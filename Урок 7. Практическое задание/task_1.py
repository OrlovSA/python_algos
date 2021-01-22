"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit

def bubble_sort(lst):
    """7.08000000000028e-05"""
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n += 1
    return lst


def my_bubble_sort(lst):
    """из цикла убран len, добавлена проверка на досрочный выход из цикла.
    2.4200000000001998e-05"""
    n = len(lst) - 1
    while True:
        x = 0
        for i in range(n):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                x = 1
        else:
            if x == 0:
                return lst
        n -= 1


lst = [random.randint(-100, 100) for _ in range(10)]
print(lst)
print(bubble_sort(lst))
print(my_bubble_sort(lst))
print(timeit.timeit("bubble_sort(lst)",
                    setup="from __main__ import bubble_sort, lst",
                    number=10)) # 7.08000000000028e-05
print(timeit.timeit("my_bubble_sort(lst)",
                    setup="from __main__ import my_bubble_sort, lst",
                    number=10)) # 2.4200000000001998e-05
