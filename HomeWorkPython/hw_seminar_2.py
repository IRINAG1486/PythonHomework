# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
'''
number_1 = int(input('Input your number: '))

degree = 1
number_2 = 2
rez = 0

while rez <= number_1:
    rez = number_2 ** degree
  
    if rez <= number_1:
        print(f'For degree {degree} number is {rez}')
    degree += 1
'''
'''
number_1 = int(input('Input your number: '))

degree = 1
number_2 = 1
rez = 0

while number_2 <= number_1:
    number_2 *= 2
    
    if number_2 <= number_1:
        print(f'For degree {degree} number is {number_2}')
    degree += 1
'''

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
'''
sum = int(input('Input sum of two numbers: '))
mult = int(input('Input product of two numbers: '))


for x in range(sum):
    for y in range(sum):
        if x + y == sum and x * y == mult :
            print(f'Your numbers is {x} and {y}')

'''

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.
import random
count_of_coins = int(input('Input count of coins'))
coins_gerb = 0
coins_resh = 0
for i in range(count_of_coins):
    coins = random.randint(0, 1)
    print (coins)
    if coins == 1:
        coins_gerb += 1
    else:
        coins_resh += 1
if coins_gerb == coins_resh:
    print(f'You can turn coins with gerb or reshca in ammount of {coins_gerb} - ammount is equal')
elif coins_gerb == count_of_coins or coins_resh == count_of_coins:
    print(f'You do not need to turn coins')   
elif coins_gerb < coins_resh:
    print(f'Minimal counts of coins which you need to turn - {coins_gerb} and it is coins with gerb')
else:
    print(f'Minimal counts of coins which you need to turn - {coins_resh} and it is coins with reshca')

    