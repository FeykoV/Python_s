# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.


# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

from tabulate import tabulate

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('text.txt')

    while(choice != 6):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('text.txt', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        choice = show_menu()
    
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Показать весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить нового абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice
    
def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding = 'utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                    s += v + ','
            fout.write(f'{s[:-1]}\n')

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Такой абонент отстутствует"

def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
        return "Такой абонент отсутствует"
    
def add_user(data: list, user_data: str):
    fields = ["Фамилия","Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def get_search_name():
    return input("Введите фамилию: ")

def get_search_number():
    return input("Введите номер телефона:")

def get_new_user():
    return input("Введите Фамилию, Имя, номер телефона и описание через запятую: ")

def get_file_name():
    return input("Введите название файла: ")

def print_result(phone_book):
    print(tabulate(phone_book))

work_with_phonebook()