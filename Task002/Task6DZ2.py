# Знакомство с языком Python (семинары)
# Урок 6. Повторение списков

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).

from random import randint
import random

array = [random.randint(-10, 10) for i in range(10)]
print('Ввод 1 - Заполняем заданный массив', array)

min_number = randint(-10, -1)
print('Ввод 2 - Минимальное значение =', min_number)
max_number = randint(1, 10)
print('Ввод 3 - Максимальное значение =', max_number)

new_array = [i for i in array if min_number <= i <= max_number]
print('Ввод 4 - Заполняем новый массив:', new_array)

def index_array(new_array):
    print('Ответ - Индексы элементов массива:')
    for i in new_array:
        index = array.index(i)
        print(index, end=" ")

index_array(new_array)