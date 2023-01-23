import os


# ФУНКЦИЯ СОЗДАНИЯ ФАЙЛА ДЛЯ БАЗЫ ДАННЫХ СПРАВОЧНИКА
def create_directory():
    if os.path.exists('Phone_dictionary.txt') is not True:
        temp = open('Phone_dictionary.txt', 'w', encoding="utf-8")
        temp.close()

# ФУНКЦИЯ ПРОСМОТРА ИМЕЮЩИХСЯ КОНТАКТОВ 
def view_entry():
    temp_lst = []
    with open('Phone_dictionary.txt', 'r', encoding='utf-8') as file:
        for line_numb, line in enumerate(file, start=1):
            temp_lst.append(str(line_numb) + '. ' + line[:(-1)])
    return line_numb, temp_lst

# ФУНКЦИЯ ДОБАВЛЕНИЯ НОВЫХ КОНТАКТОВ В БАЗУ ДАННЫХ
def add_entry(add_str=str):
    with open('Phone_dictionary.txt', 'a', encoding='utf-8') as file:
        file.write(add_str)
    return

# ФУНКЦИЯ ПОИСКА КОНТАКТОВ
def find_entry(find_str=str):
    result_find = []
    with open('Phone_dictionary.txt', 'r', encoding='utf-8') as file:
        for line_numb, line in enumerate(file, start=1):
            if find_str in line:
                result_find.append(str(line_numb) + '. ' + line[:(-1)])
    return result_find

# ФУНКЦИЯ УДАЛЕНИЯ КОНТАКТОВ
def del_entry(del_line=int):
    with open('Phone_dictionary.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    del lines[del_line - 1]
    with open('Phone_dictionary.txt', 'w', encoding='utf-8') as file:
        file.writelines(lines)
    pass
