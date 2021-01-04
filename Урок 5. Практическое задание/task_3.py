"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
import timeit



def deque_appendleft():
    """ 0.06366440000000001 """
    d = deque()
    for i in range(10000):
        d.appendleft(i)


def list_insert():
    """2.1175042"""
    l = list()
    for i in range(10000):
        l.insert(0, i)
"""Операция вставки deque быстрее, чем в list"""


def deque_append():
    """0.5316341000000002"""
    d = deque()
    for i in range(10000):
        d.append(i)


def list_append():
    """0.5206648999999999"""
    l = list()
    for i in range(10000):
        l.append(i)
"""Операция вставки справа у list и deque выполняется примерно одинаково, 
но у списка всё же немного быстрее(на тысячные доли секунд)"""


def deque_popleft():
    """0.6096480999999998"""
    d = deque(range(1000))
    for i in range(len(d)):
        d.popleft()


def list_popleft():
    """1.7117019999999998"""
    l = list(range(1000))
    for i in range(len(l)):
        l.pop(0)
"""Операция удаления слева у deque происходит примерно в 3 раза быстрее, чем у list"""


def deque_pop():
    """0.6260647000000006"""
    d = deque(range(10000))
    for i in range(len(d)):
        d.pop()


def list_pop():
    """0.5888529"""
    l = list(range(10000))
    for i in range(len(l)):
        l.pop()
"""Операция удаления справа у deque немного медленнее, чем у list"""


def deque_insert():
    """0.11069589999999963"""
    d = deque()
    for i in range(10000):
        d.insert(0,i)


def list_insert():
    """2.0780490999999994"""
    l = list()
    for i in range(10000):
        l.insert(0, i)
"""Операция вставки слева(insert) у deque выполняется также в 40 раз быстрее, чем в list"""


print("deque_appendleft: ", timeit.timeit("deque_appendleft()", "from __main__ import deque_appendleft", number=100))
print("list_appendleft: ", timeit.timeit("list_insert()", "from __main__ import list_insert", number=100))

print("deque_append: ", timeit.timeit("deque_append()", "from __main__ import deque_append", number=1000))
print("list_append: ", timeit.timeit("list_append()", "from __main__ import list_append", number=1000))

print("deque_popleft: ", timeit.timeit("deque_popleft()", "from __main__ import deque_popleft", number=10000))
print("list_popleft: ", timeit.timeit("list_popleft()", "from __main__ import list_popleft", number=10000))

print("deque_pop: ", timeit.timeit("deque_pop()", "from __main__ import deque_pop", number=1000))
print("list_pop: ", timeit.timeit("list_pop()", "from __main__ import list_pop", number=1000))

print("deque_insert: ", timeit.timeit("deque_insert()", "from __main__ import deque_insert", number=100))
print("list_insert: ", timeit.timeit("list_insert()", "from __main__ import list_insert", number=100))

"""
Вывод: у deque операции и удаления в начало сложность равна O(1) - согласно различным статьям на различных сайтах
, а у списка обратная ситуация: вставка/удалиние в/из начала имеет сложность O(n), 
но в операциях по извлечению значения(случайный доступ), у списка происходит быстрее чем в deque.
"""