# Задача 2.
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

import random 
'''
num_1 = random.randint(10, 20)
num_2 = random.randint(10, 20)
print(num_1, num_2)

def find_sum (num_a, num_b):
    if num_b == 0:
        return num_a
    return(find_sum(num_a + 1, num_b - 1))

print (find_sum(num_1, num_2))
'''
# Задача 1.
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.


first_num = random.randint(2, 5)
second_num = random.randint(2, 5)
print(first_num, second_num)

def make_degrre(num_a, num_b):
    if num_b == 1:
        return num_a
    return(make_degrre(num_a, num_b - 1) * num_a)

print(make_degrre(first_num, second_num))
