# Задача 6. Спецшифр
# Что нужно сделать
# Два сотрудника спецслужб переписываются необычным шифром. Каждую букву они шифруют в виде строки, внутри которой
# есть длинная последовательность букв s, а длина самой длинной — это и есть номер буквы алфавита, которую хотят
# отправить.
# Напишите программу, которая получает на вход строку, подсчитывает в ней самую длинную последовательность идущих
# подряд букв s и выводит ответ на экран.
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

max_count = 0
count_sym = 0
prev_sym = ''

text = input('Enter the text: ')
for sym in text:
    if prev_sym == sym:
        count_sym += 1
        if max_count < count_sym:
            max_count = count_sym
    else:
        prev_sym = sym
        count_sym = 1
print('larges sequence is', max_count)
