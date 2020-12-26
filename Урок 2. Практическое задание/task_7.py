"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

 Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def input_check():
    while True:
        try:
            num = int(input('Введите число:\n'))
            return multitudes(num)
        except ValueError:
            print('Неверный ввод.')


def multitudes(num, i=1, n=1):
    if num == n:
        return print(num, i, num * (num + 1) // 2)
    return multitudes(num, i+n+1, n+1)


input_check()