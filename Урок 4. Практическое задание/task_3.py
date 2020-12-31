"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    """Самый эфективный, судя по значениям"""
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


cProfile.run('revers(876487264876238946384759823)')
print(timeit(
        'revers(876487264876238946384759823)',
        setup='from __main__ import revers',
        number=10000)) # 0.1291524

cProfile.run('revers_2(876487264876238946384759823)')
print(timeit(
        'revers_2(876487264876238946384759823)',
        setup='from __main__ import revers_2',
        number=10000)) # 0.09067910000000001

cProfile.run('revers_3(876487264876238946384759823)')
print(timeit(
        'revers_3(876487264876238946384759823)',
        setup='from __main__ import revers_3',
        number=10000)) # 0.006499299999999986