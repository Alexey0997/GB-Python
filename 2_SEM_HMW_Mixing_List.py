# Задача № 3.	Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int.

print("\n")
my_list = []                          # Инициализируем исходный список. 
for i in range(1, 20, 2):             # Зададим значения элементовв диапазоне [1, 19] 
    my_list.append(i)                 # с шагом +2.
print(f'Исходный список:     {my_list}.') 

import random
def new_list(my_list):                # Перемешивание списка.
    new_list = my_list[:]             # Создадим копию списка.    
    new_list_length = len(new_list)   # Определим длину списка.
    for i in range(new_list_length):  # Сгенерируем случайный индекс.
        index = random.randint(0, new_list_length - 1)
        temp = new_list[i]            # Запишем во временный файл знач. сген. эл-та.
        new_list[i] = new_list[index] # Присвоим i-му элементу значение сген. эл-та.
        new_list[index] = temp        # На место, имеющее сген index в новом списке 
    return new_list                   # положим значение из временного файла.  
new_list = new_list(my_list)          # Новому списку присвоим результат метода.
print(f'Перемешанный список: {new_list}.') 