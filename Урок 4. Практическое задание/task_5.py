"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
from timeit import timeit


#O(n^2)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


def sieve(n):
    """«Решета Эратосфена»"""
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    return a


for i in [10, 100, 1000]:
    print(f'Старт с числом {i}' + ('-' * 100))
    print(f'simple-------------')
    print(simple(i))
    print(timeit(
            f'simple({i})',
            setup='from __main__ import simple',
            number=10000)) # 10 - 0.1725824, 100 - 15.193614, 1000 - 2711.9046375
    print(f'sieve--------------')
    print(sieve(i))
    print(timeit(
            f'sieve({i})',
            setup='from __main__ import sieve',
            number=10000)) # 10 - 0.023565099999999978, 100 - 0.19594990000000045, 1000 - 3.4842837000001055

"""Судя по замерам, выгодней использовать Решета Эратосфена на больших числах"""