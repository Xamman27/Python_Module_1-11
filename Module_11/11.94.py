# Задача 4. Крест
# Что нужно сделать
# Напишите программу, которая выводит на экран крест из символов «^»
# (символы выводятся по диагоналям воображаемого квадрата).
for col in range(10):
    for row in range(10):
        if row == col or row  == -col + 9 :
            print('^', end=' ')
        else:
            print(' ', end=' ')
    print()