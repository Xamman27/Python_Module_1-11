# Задача 1. Электронная очередь
#
# Нам дали заказ написать программу для электронной очереди. У каждого человека в очереди есть номер:
# нулевой, первый, второй, третий и так далее. Каждый час очередь уменьшается на одного человека, то есть уходит
# сначала нулевой номер, затем первый, второй и так далее. Наша программа получает на вход одно число — количество
# людей в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.

people = int(input('Enter the number of people in the queue: '))
for hour in range(people + 1):
    print(hour ,"hour o'clock goes")
    for person in range(hour, people + 1):
        print('Number in queue', person)
    print()
print('The queue is over')
