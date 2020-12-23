"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""

rev_num = ''


def input_check():
    while True:
        try:
            num = int(input('Введите число:\n'))
            if len(str(num)) <= 1:
                print('В числе должно быть больше 1 цифры')
            else:
                return num_revers(str(num))
        except ValueError:
            print('Неверный ввод.')


def num_revers(n):
    global rev_num
    i = len(n)
    if len(n) == 0:
        return print(rev_num)
    else:
        rev_num += n[-1]
    return num_revers(n[:i-1])


input_check()