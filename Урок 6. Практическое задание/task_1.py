"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
from memory_profiler import profile
from collections import deque

"""Python 3.8, win10-64x"""

@profile
def deque_appendleft():
    """
    0.06366440000000001

        Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    21     19.3 MiB     19.3 MiB           1   @profile
    22                                         def deque_appendleft():
    24     19.3 MiB      0.0 MiB           1       d = deque()
    25     19.6 MiB      0.0 MiB       10001       for i in range(10000):
    26     19.6 MiB      0.3 MiB       10000           d.appendleft(i)
    """
    d = deque()
    for i in range(10000):
        d.appendleft(i)

@profile
def list_insert():
    """
    2.1175042

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    89     19.6 MiB     19.6 MiB           1   @profile
    90                                         def list_insert():
    92     19.6 MiB      0.0 MiB           1       l = list()
    93     19.8 MiB      0.0 MiB       10001       for i in range(10000):
    94     19.8 MiB      0.2 MiB       10000           l.insert(0, i)
    """
    l = list()
    for i in range(10000):
        l.insert(0, i)
"""Операция вставки deque быстрее, чем в list но deque больще занимает памяти."""

@profile
def deque_append():
    """
    0.5316341000000002

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    36     19.8 MiB     19.8 MiB           1   @profile
    37                                         def deque_append():
    39     19.8 MiB      0.0 MiB           1       d = deque()
    40     19.8 MiB      0.0 MiB       10001       for i in range(10000):
    41     19.8 MiB      0.0 MiB       10000           d.append(i)
    """
    d = deque()
    for i in range(10000):
        d.append(i)

@profile
def list_append():
    """
    0.5206648999999999

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    43     19.8 MiB     19.8 MiB           1   @profile
    44                                         def list_append():
    46     19.8 MiB      0.0 MiB           1       l = list()
    47     19.8 MiB      0.0 MiB       10001       for i in range(10000):
    48     19.8 MiB      0.0 MiB       10000           l.append(i)
    """
    l = list()
    for i in range(10000):
        l.append(i)
"""Операция вставки справа у list и deque выполняется примерно одинаково, 
но у списка всё же немного быстрее(на тысячные доли секунд)
по памяти занимают одинаково"""

@profile
def deque_popleft():
    """
    0.6096480999999998
    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    52     19.8 MiB     19.8 MiB           1   @profile
    53                                         def deque_popleft():
    55     19.8 MiB      0.0 MiB           1       d = deque(range(1000))
    56     19.8 MiB      0.0 MiB        1001       for i in range(len(d)):
    57     19.8 MiB      0.0 MiB        1000           d.popleft()
    """
    d = deque(range(1000))
    for i in range(len(d)):
        d.popleft()

@profile
def list_popleft():
    """
    1.7117019999999998

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    59     19.8 MiB     19.8 MiB           1   @profile
    60                                         def list_popleft():
    62     19.8 MiB      0.0 MiB           1       l = list(range(1000))
    63     19.8 MiB      0.0 MiB        1001       for i in range(len(l)):
    64     19.8 MiB      0.0 MiB        1000           l.pop(0)
    """
    l = list(range(1000))
    for i in range(len(l)):
        l.pop(0)
"""Операция удаления слева у deque происходит примерно в 3 раза быстрее, чем у list
по памяти занимают одинаково"""

@profile
def deque_pop():
    """
    0.6260647000000006

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    67     19.8 MiB     19.8 MiB           1   @profile
    68                                         def deque_pop():
    70     19.8 MiB      0.0 MiB           1       d = deque(range(10000))
    71     19.9 MiB      0.0 MiB       10001       for i in range(len(d)):
    72     19.9 MiB      0.0 MiB       10000           d.pop()
    """
    d = deque(range(10000))
    for i in range(len(d)):
        d.pop()

@profile
def list_pop():
    """
    0.5888529

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    74     19.9 MiB     19.9 MiB           1   @profile
    75                                         def list_pop():
    77     19.9 MiB      0.0 MiB           1       l = list(range(10000))
    78     19.9 MiB      0.0 MiB       10001       for i in range(len(l)):
    79     19.9 MiB      0.0 MiB       10000           l.pop()
    """
    l = list(range(10000))
    for i in range(len(l)):
        l.pop()
"""Операция удаления справа у deque немного медленнее, чем у list
deque занимает меньше памяти"""

@profile
def deque_insert():
    """
    0.11069589999999963

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    82     19.9 MiB     19.9 MiB           1   @profile
    83                                         def deque_insert():
    85     19.9 MiB      0.0 MiB           1       d = deque()
    86     19.9 MiB      0.0 MiB       10001       for i in range(10000):
    87     19.9 MiB      0.0 MiB       10000           d.insert(0,i)
    """
    d = deque()
    for i in range(10000):
        d.insert(0,i)

@profile
def list_insert():
    """
    2.0780490999999994

    Line #    Mem usage    Increment  Occurences   Line Contents
    ============================================================
    89     19.9 MiB     19.9 MiB           1   @profile
    90                                         def list_insert():
    92     19.9 MiB      0.0 MiB           1       l = list()
    93     19.9 MiB      0.0 MiB       10001       for i in range(10000):
    94     19.9 MiB      0.0 MiB       10000           l.insert(0, i)
    """
    l = list()
    for i in range(10000):
        l.insert(0, i)
"""Операция вставки слева(insert) у deque выполняется также в 40 раз быстрее, чем в list
по памяти занимают одинаково"""


print("deque_appendleft: ", timeit.timeit("deque_appendleft()", "from __main__ import deque_appendleft", number=1))
print("list_appendleft: ", timeit.timeit("list_insert()", "from __main__ import list_insert", number=1))

print("deque_append: ", timeit.timeit("deque_append()", "from __main__ import deque_append", number=1))
print("list_append: ", timeit.timeit("list_append()", "from __main__ import list_append", number=1))

print("deque_popleft: ", timeit.timeit("deque_popleft()", "from __main__ import deque_popleft", number=1))
print("list_popleft: ", timeit.timeit("list_popleft()", "from __main__ import list_popleft", number=1))

print("deque_pop: ", timeit.timeit("deque_pop()", "from __main__ import deque_pop", number=1))
print("list_pop: ", timeit.timeit("list_pop()", "from __main__ import list_pop", number=1))

print("deque_insert: ", timeit.timeit("deque_insert()", "from __main__ import deque_insert", number=1))
print("list_insert: ", timeit.timeit("list_insert()", "from __main__ import list_insert", number=1))

