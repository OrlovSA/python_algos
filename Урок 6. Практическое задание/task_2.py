"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""
from memory_profiler import profile


@profile
def generator_expression():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    11     19.0 MiB     19.0 MiB           1   @profile
    12                                         def generator_expression():
    13     24.0 MiB  -3583.1 MiB      100003       mylist = [x for x in range(100000)]
    14     24.0 MiB      0.0 MiB      100001       for i in mylist:
    15     24.0 MiB      0.0 MiB      100000           pass
    """
    mylist = [x for x in range(100000)]
    for i in mylist:
        pass


@profile
def generator():
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    18     19.0 MiB     19.0 MiB           1   @profile
    19                                         def generator():
    20     19.0 MiB      0.0 MiB      200003       mygenerator = (x for x in range(100000))
    21     19.0 MiB      0.0 MiB      100001       for i in mygenerator:
    22     19.0 MiB      0.0 MiB      100000           pass
    """
    mygenerator = (x for x in range(100000))
    for i in mygenerator:
        pass


def yield_generator():
    mylist = range(100000)
    for i in mylist:
        yield i


@profile
def yield_generator_iter(l):
    """
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    32     19.0 MiB     19.0 MiB           1   @profile
    33                                         def yield_generator_iter(l):
    34     19.0 MiB      0.0 MiB      100001       for i in l:
    35     19.0 MiB      0.0 MiB      100000           pass
    """
    for i in l:
        pass



generator_expression()
generator()
gen = yield_generator() # создаём генератор
yield_generator_iter(gen)