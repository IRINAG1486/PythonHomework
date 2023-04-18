# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

dict_engl = {'A, E, I, O, U, L, N, S, T, R': '1', 'D, G': '2', 'B, C, M, P': '3', 'F, H, V, W, Y': '4', 'K': 5, 'J, X': '8', 'Q, Z': '10'}

dict_rus = {'А, В, Е, И, Н, О, Р, С, Т': '1', 'Д, К, Л, М, П, У': '2', 'Б, Г, Ё, Ь, Я': '3', 'Й, Ы': '4', 'Ж, З, Х, Ц, Ч': '5', 'Ш, Э, Ю': '8', 'Ф, Щ, Ъ': '10'}

rus_exempl = 'ЙУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'

eng_exempl = 'QWERTYUIOPASDFGHJKLZXCVBNM'

your_world = input('Input your world in English or Russian language: ')

print(your_world)

sum = 0

if your_world[0] in eng_exempl:
    
    for i in your_world:
        for (key, value) in dict_engl.items():
            if i in key:
                sum += int(value)
    print(f'Cost of your word is {sum}')

else: 
    if your_world[0] in rus_exempl:
    
        for i in your_world:
            for (key, value) in dict_rus.items():
                if i in key:
                    sum += int(value)
         
    print(f'Cost of your word is {sum}')



# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
'''
list_size = int(input('Input size of your list: '))

find_number = int(input('Input number for search: '))

list_1 = [random.randint(0, 10) for _ in range(list_size)]
print(list_1)
count = 0
for i in list_1:
    if i == find_number:
        count += 1
print(f'You can meet {find_number} in list {count} times')
'''

# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
'''
list_size = int(input('Input size of list: '))
find_number = int(input('Input number for count: '))

list_1 = [random.randint(0, 20) for _ in range(list_size)]
print(list_1)

min = abs(list_1[0] - find_number)
index = 0

for i in range(list_size):

    next_num = abs(list_1[i] - find_number)
    if next_num < min:
        min = next_num
        index = i
print(f'The closest number for {find_number} is {list_1[index]}')
'''