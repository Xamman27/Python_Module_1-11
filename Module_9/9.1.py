"""
Задача 1. Космическая еда

Что нужно сделать
Ваш космический корабль потерпел крушение на пустынной планете. Еда здесь не растёт, но вы спасли из
обломков 100-килограммовый мешок гречки. Из прошлого опыта вы знаете, что если будете экономно питаться,
то у вас будет уходить по четыре килограмма гречки в месяц.

Чтобы прикинуть гречневый бюджет, вы решили написать программу, которая выведет информацию о том,
сколько килограммов гречки у вас должно быть в запасе через месяц, два и так далее, пока она не закончится.
Используйте цикл for.
"""
total_month = 0
for remainder in range(100, 0, -4):
    total_month += 1
    print('You lived', total_month, 'month')
    print('leftover buckwheat', remainder)
    print('')
