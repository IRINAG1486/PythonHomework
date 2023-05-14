# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

'''
start_num = int(input("Input first number of range: "))
step = int(input("Input step of elements in range: "))
your_count = int(input("Input count elements in range: "))

for i in range(start_num, start_num + step * your_count, step):
    print(i, end= " ")
'''

# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

list_1 = [random.randint(1, 30) for _ in range(10)]
print( list_1)

min_num = int(input('Input min number of range: '))
max_num = int(input('Input max number of range: '))

new_list = []

for i in range(len(list_1)):
    if list_1[i] > min_num and list_1[i] < max_num:
        new_list.append(i)
print(new_list)
