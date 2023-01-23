from Model import *


# ФУНКЦИЯ УПРАВЛЕНИЯ ГЛАВНЫМ МЕНЮ
def main_menu():
    create_directory()
    print('\nГлавное меню:\n'
          '\tДействия со справочником - 1\n'
          '\tВыход из программы       - 2 ')
    num_menu = input(f'\tВведите номер задачи: ')
    lst_num = ['1', '2']
    if check_menu(num_menu, lst_num) is True:
        if num_menu == '2':
            print('\nРабота справочника завершена.')
        elif num_menu == '1':
            menu_action()
    else:
        print(f'\nЧисло "{num_menu}" является некорректным.\n')
        main_menu()  
    return

# ФУНКЦИЯ УПРАВЛЕНИЯ МЕНЮ РАБОТЫ С ТЕЛЕФОННЫМ СПРАВОЧНИКОМ
def menu_action():
    print('\nДействия со справочником: \n'
          '\tПросмотр записей         - 1\n'
          '\tДобавление записи        - 2\n'
          '\tПоиск записи             - 3\n'
          '\tУдаление записи          - 4\n'
          '\tВозврат в главное меню   - 5\n'
          '\tСохранение - автоматическое.')
    lst_num = ['1', '2', '3', '4', '5']
    num_menu = input(f'\tВведите номер задачи: ')
    if check_menu(num_menu, lst_num) is True:
        if num_menu == '1':    # Вызов списка контактов. 
            menu_view()
            menu_action()
        elif num_menu == '2':  # Добавление нового контакта. 
            menu_add()
            menu_action()
        elif num_menu == '3':  # Поиск абонентов. 
            menu_search()
            menu_action()
        elif num_menu == '4':  # Удаление контактов. 
            menu_del()
            menu_action()
        elif num_menu == '5':  # Возврат в главное меню. 
            main_menu()
    else:                      # Сообщение при вводе некорректного числа. 
        print(f" \nВведено некорректное значение: {num_menu}  \n")
        main_menu()
    return

# ФУНКЦИЯ ПРОВЕРКИ ПРАВИЛЬНОСТИ ВВОДА ДАННЫХ 
def check_menu(num, lst_): # Требуется ввести однозначное число, имеющееся в списке.
    if len(num) == 1 and num.isdigit() is True and num in lst_:
        return True
    else:
        return False

# ФУНКЦИЯ ВЫВОДА СПИСКА АБОНЕНТОВ
def menu_view():
    print('\nТелефонный справочник:\n')
    last_num, lst_tel = view_entry()
    for view in lst_tel:
        print(view) 

# ФУНКЦИЯ ДОБАВЛЕНИЯ НОВОГО КОНТАКТА
def menu_add():
    add_str = (input(f'\nВведите имя: ') + ' ' +
               input(f'Введите фамилию: ') + ' ' +
               input(f'Введите номер: ') + ' ' +
               input(f'Введите комментарий: ') + '\n')
    add_entry(add_str)

# ФУНКЦИЯ ПОИСКА КОНТАКТА
def menu_search():
    find_str = input(f'\nВведите данные для поиска: ')
    if len(find_entry(find_str)) == 0:
        print(f'\nСведениями о {find_str} не располагаем.')
    else:
        for find_line in find_entry(find_str):
            print(f'В справочнике имеются следующие сведения об абоненте:\n\
            {find_line}')

# ФУНКЦИЯ УДАЛЕНИЕ КОНТАКТОВ
def menu_del():
    last_num, lst_tel = view_entry()  # Демонстрация списка абонентов.
    print('\nТелефонный справочник:')
    for view in lst_tel:
        print(view)                   # Предложение удалить по номеру контакта.
    delete_num = input('\nВведите порядковый номер контакта, который хотите удалить: ')
    if delete_num.isdigit() is True and int(delete_num) <= last_num:
        temp_del = input("\nВы действительно хотите удалить контакт? Да/Нет: ")
        if temp_del in ['Да', 'да']:
            del_entry(int(delete_num))
    else:
        print(f'Введен некорректный номер: {delete_num}')
