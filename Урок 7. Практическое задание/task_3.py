"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

import random
from statistics import median


def find_m(i):
    left = []
    right = []
    for n, val in enumerate(lst):
        if val <= lst[i] and n != i:
            left.append(val)
        elif val >= lst[i] and n != i:
            right.append(val)
    if len(left) == len(right):
        return True


m = 10
lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(lst)

for n, val in enumerate(lst):
    if find_m(n):
        print(lst[n])

print(median(lst))


