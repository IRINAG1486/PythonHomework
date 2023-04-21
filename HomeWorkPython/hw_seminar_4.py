# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
#Вариант 1. 
import random 
'''
size_1 = int(input('Input size of first list: '))
size_2 = int(input('Input size of second list: '))

set_1 = {i ** 2 for i in range(size_1)}
set_2 = {i ** 2 for i in range(size_2)}

print(set_1)
print(set_2)

new_set = set_1.intersection(set_2)
print(new_set)

new_list = list(new_set)

new_list.sort()
print(new_list)
'''

#Вариант 2.
'''
size_1 = int(input('Input size of first list: '))
size_2 = int(input('Input size of second list: '))

list_1 = [random.randint(0, 10) for _ in range(size_1)]
list_2 = [random.randint(0, 10 ) for _ in range(size_2)]

set_1 = set(list_1)
set_2 = set(list_2)

print(set_1)
print(set_2)

new_set = set_1.intersection(set_2)
print(new_set)

new_list = list(new_set)

end_list = list()
for i in range(len(new_list)-1):
    for j in range(len(new_list)-1):
        if new_list[j] > new_list[j+1]:
            
            
            new_list[j], new_list[j+1]  = new_list[j+1], new_list[j]
        
print(new_list)
'''


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.


bush_count = int(input('Input count of bushes:'))

list_1 = [random.randint(1, 10) for _ in range(bush_count)]
print(list_1)

list_2 = list()

for i in range(len(list_1)):
    list_2.append(list_1[i-2] + list_1[i-1] + list_1[i] )
    print(list_2)
print(max(list_2))


    
 