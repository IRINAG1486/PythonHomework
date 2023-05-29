phonebook = 'phonebook.txt'
phone_list = []
new_list = []

#показать контакты
def show_contacts():
    for line in phone_list:
        line = line.split()
        new_list.append(line)
        print(f'Name: {line[0]}/ Middle name: {line[1]}/ Second name: {line[2]}/ Phone number: {line[3]}')
#show_contacts()

#открыть файл
def open_file():
    with open(phonebook, 'r', encoding='utf-8') as file:

        for line in file:
            line = line.strip()
            
            phone_list.append(line)
        #print(phone_list)
        print('Phonebook is opened')
#open_file()

#добавить контакт
def add_contact():
    first_name = input('Input first name: ')
    new_list.append(first_name.lower())
    middle_name = input('Input middle name: ')
    new_list.append(middle_name.lower())
    second_name = input('Input second name: ')
    new_list.append(second_name.lower())
    phone_number = input('Inpyt phone number: ')
    new_list.append(phone_number)
    print(f"\n{new_list[0]} {new_list[1]} {new_list[2]} {new_list[3]}\n")
    
def add_contact_in_file():
    with open(phonebook, 'a', encoding='utf-8') as file:
        file.write(' '.join(new_list) + '\n' )
        print(file)
        print('Контакт добавлен в телефонную книгу')
#add_contact()
#add_contact_in_file()


#найти контакт
def find_contact(): 
    finding_data = input('Введите одно из данных контакта, который необходимо найти: ').lower()
    for i in phone_list:
        if finding_data in i:
            res = i.split()
            print(f" Name: {res[0]}/ Middle name: {res[1]}/ Second name: {res[2]}/ Phone number: {res[3]}")

#find_contact()

#удалить контакт
def del_contact(): 
    data_for_delete = input('Введите одно из данных контакта, который необходимо удалить: ').lower()
    for i in phone_list:
        if data_for_delete not in i:
            new_list.append(i)
    print(new_list)
    print('Контакт удален')
    print('Выберите пункт меню "2", чтобы записать изменения')
#del_contact()

#записать файл
def write_file():
    with open(phonebook, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_list))
        print('Phonebook is changed')


#изменить контакт
def change_contact():
    new_data = []
    changing_data = str(input('Введите одно из данных контакта, который необходимо изменить: ').lower())
    first_name = input('Input first name: ')
    new_data.append(first_name.lower())
    middle_name = input('Input middle name: ')
    new_data.append(middle_name.lower())
    second_name = input('Input second name: ')
    new_data.append(second_name.lower())
    phone_number = input('Inpyt phone number: ')
    new_data.append(phone_number)
    new_data = ' '.join(new_data)
    for i in range(len(phone_list)):
        if changing_data in phone_list[i]:
            phone_list[i] = new_data
    for i in phone_list:
        new_list.append(i)     
    print(new_list)
    print('Контакт изменен')
    print('Выберите пункт меню "2", чтобы записать изменения')
        

#change_contact()                 


def show_menu():
    print('''\n Меню:
          1. Открыть файл
          2. Записать файл
          3. Показать контакт
          4. Добавить контакт
          5. Найти контакт
          6. Изменить контакт
          7. Удалить контакт
          8. Выход\n''')
 
    while True:
        menu = int(input('Введите пункт меню: '))
        if menu > 0 and menu < 9:
            if menu == 1:
                open_file()
            elif menu == 2:
                write_file()
            elif menu == 3:
                show_contacts()
            elif menu == 4:
                add_contact()
                add_contact_in_file()
            elif menu == 5:
                find_contact()
            elif menu == 6:
                del_contact()
            elif menu == 7:
                change_contact()
            elif menu == 8:
                print('Работа завершена')
                break
        else:
            print('Error! Input number!')
show_menu()