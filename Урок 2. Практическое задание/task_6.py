"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint


def input_check(min_num, max_num, attempts):
    while True:
        try:
            num = int(input(f'У вас {attempts} попыток\nВведите число:\nБольше {min_num} меньше {max_num}\n:'))
            if num >= max_num:
                print('Число больше диапазона')
            elif num <= min_num:
                print('Число меньше диапазона')
            else:
                return num
        except ValueError:
            print('Неверный ввод.')


def game(num, attempts=10, min_num=1, max_num=100):
    if attempts == 0:
        return print(f"Число было {num}")
    num_user = input_check(min_num, max_num, attempts)
    if num_user != num:

        if num_user > num:
            max_num = num_user
        else:
            min_num = num_user
        return game(num, attempts-1, min_num, max_num)
    else:
        return print('Вы отгодали!')


game(randint(1, 101))