"""
Вася вдохновился фильмом «Двадцать одно» и решил изучить математику
игровых автоматов. Для анализа данных ему нужна информация о том,
как часто в автомате выпадает три или две одинаковых картинки.
Для сбора данных нужна программа, проверяющая это равенство.

Даны три целых числа. Определите, сколько среди них совпадающих.
Программа должна вывести одно из чисел: 3 (если все совпадают),
2 (если два совпадают) или 0 (если все числа разные).

Советы и рекомендации
По возможности уделите внимание сокращению кода. Избегайте проверки
условий, которые уже проверены: если вы проверили условие condition,
то не следует проверять not condition.
"""
num_1 = int(input('Enter the first number: '))
num_2 = int(input('Enter the first second: '))
num_3 = int(input('Enter the first third: '))
if num_1 == num_2 and num_2 == num_3:
    print('3')
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print('2')
else:
    print('0')