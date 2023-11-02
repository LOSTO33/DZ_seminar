# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os



def print_data():
    with open("phonebook.txt","r",encoding="utf-8") as file:
        phonebook_str = file.read()
    print(phonebook_str)
    print()


def input_name():
    return input("Введите имя контакта: ").title()

def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите номер телефона контакта: ")

def input_address():
    return input("Введите аадрес контакта: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep =" "  
    return  f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}\n{address}\n\n"

def add_contact():
    new_contact_str = input_data()
    with open("phonebook.txt","a",encoding="utf-8") as file:
        file.write(new_contact_str)


def search_contact():
    print("Варианты поиска:\n"
        "1.По фамилии\n"
        "2.По имени\n"
        "3.По отчеству\n"
        "4.По телефону\n"
        "5.По адресу\n")
    command = input("Выберите вариант поиска: ")
    
    while command not in ("1", "2", "3", "4","5"):
        print("Некоректные ввод повториет запрос ")
        command = input("Выберите вариант поиска: ")
    
    i_search = int(command)-1
    search = input("Введите данные для поиска: ").lower()
    print()

    with open("phonebook.txt","r",encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split("\n\n")
        
    check_cont = False
    for contact_str in contacts_list:
        lst_contact = contact_str.lower().replace("\n", " ").split() 
        if search in lst_contact[i_search]:
            print (contact_str)
            print()
            check_cont = True

    if not check_cont:
        print("Такого контакта нет.")



def changes_contact():
    last_name = input("Ведите Имя и фамилию контакта : ")
    if last_name in contact_list:
        new_name = input("Введите новый ")
        contact_list[last_name] = new_name
        print(contact_list)





def interface():
    with open("phonebook.txt","a",encoding="utf-8"):
        pass
    command = ""
    os.system("cls")
    while command !="6":
        print("Меню пользователя:\n"
            "1.Вывод данных на экран\n"
            "2.Добавить контакт\n"
            "3.Поиск контакта\n"
            "4.Изменть контакт\n"
            "5.Удалить контакт\n"
            "6.Выход\n")
        command = input("Выбериет пункт меню: ")
        
        while command not in ("1", "2", "3", "4","5","6"):
            print("Некоректные ввод повториет запрос ")
            command = input("Ввыбериет пункт меню ")
        match command:
            case "1":
                print_data()
            case "2":
                add_contact()
            case "3":
                search_contact()
            case "4":
                changes_contact()
            case "5"
                delete_contact()
            case "6":
                print("Завершение программы")
        print()


if __name__ == "__main__":
    interface()