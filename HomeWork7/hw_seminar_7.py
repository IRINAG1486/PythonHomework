# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_columns):
    new_list = list([operation(i, j) for i in range(1, num_rows + 1)] for j in range(1, num_columns + 1))
    print(new_list)

    for i in new_list: 
        print(*(f"{j: ^5}" for j in i))
        
print_operation_table(lambda x, y: x * y, 6, 6)


# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

'''
my_frase = 'пара-ра-рам рам-пам-папам па-ра-па-дам дам'

vowel = ['й','у','е','ы','а','о','э','я','и','ю']

characteristic = lambda object: sum(1 for i in object if i in vowel)

def if_the_same(function, object):
    my_list = my_frase.split()
    print(my_list)
    new_set = set(map(function, my_list ))
    print(new_set)
    if len(new_set) == 1:
        return 'Парам-пам-пам'
    return 'Пам-парам'

print(if_the_same(characteristic, my_frase))
'''