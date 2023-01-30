# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint as r
# string = '2, 3, 5, 9, 3'
# my_list = (list(map(int, string.split(','))))
# print(my_list)
# count = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         count += my_list[i]
# print(count)

# Задайте список из n чисел последовательности (1 + 1/n)**n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# n = int(input('Введите число: '))
# list = [round((1+1/i)**i, 2) for i in range(1, n+1)]
# print(f'{list}\nСумма: {round(sum(list), 2)}')

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

def shuffle(A):
    last_index = len(A) - 1
    while last_index > 0:
        rand_index = r(0, last_index)
        A[last_index], A[rand_index] = A[rand_index], A[last_index]
        last_index -= 1
    return A

my_list = [r(0, 100) for i in range(10)]
# for i in range(10):
#     my_list.append(r(0, 100))
print(f'Список до перемешивания: {my_list}')
print(f'Список после перемешивания: {shuffle(my_list)}')
