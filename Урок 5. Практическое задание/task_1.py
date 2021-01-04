"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

from collections import namedtuple


n = int(input('Введите количество компаний: '))
company = namedtuple('companies', 'name quarter_1 quarter_2 quarter_3 quarter_4')
companies_dict = {}
for i in range(n):
    name = input('Введите название: ')
    quarter = []
    for x in range(1, 5):
        quar = float(input(f'Введите прибыль компании {name} за {x} квартал: '))
        quarter.append(quar)
    companies = company(
        name=name,
        quarter_1=quarter[0],
        quarter_2=quarter[1],
        quarter_3=quarter[2],
        quarter_4=quarter[3]
    )

    companies_dict[companies.name] = (companies.quarter_1 + companies.quarter_2 +
                                      companies.quarter_3 + companies.quarter_4)
sum_inc = 0
for val in companies_dict.values():
    sum_inc += val
avg_income = sum_inc / n
print(f'Средняя прибыль {avg_income}')
above_avg = []
below_avh = []
for key, val in companies_dict.items():
    if val > avg_income:
        above_avg.append(key)
    elif val < avg_income:
        below_avh.append(key)
print(f'Компании с прибылью ниже среднего: {", ".join(below_avh)}')
print(f'Компании с прибылью выше среднего: {", ".join(above_avg)}')

