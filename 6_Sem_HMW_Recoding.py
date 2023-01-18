# Задача № 2.	Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# НОВЫЙ МЕТОД ФОРМИРОВАНИЯ СПИСКА И ОБРАБОТКИ C LIST COMPREHENSION

from random import randint as RI         # Импорт генератора случайных чисел.
my_list = [RI(0, 20) for i in range(10)] # Создадим список из 10 случайных чисел.

my_list_length = len(my_list)            # Расчет произведения крайних чисел списка.  
prod_list = [my_list[i] * my_list[my_list_length - 1 - i] for i in range(my_list_length) if i <= my_list_length / 2 ]
print(f'\nСгенерированный список: {my_list} \nСписок произведений:    {prod_list}\n')

# РЕШЕНИЕ ЗАДАЧИ БЕЗ ИСПОЛЬЗОВАНИЯ МЕТОДОВ УСКОРЕННОЙ ОБРАБОТКИ ДАННЫХ

# print('\n')                               # Инициализация списка.
# my_list = []
# for i in range(0, 20, 3):
#     my_list.append(i)
# print(f'Сгенерированный список:   {my_list}.')

# product = 0                               # Определение пар крайних чисел 
# prod_list = []                            # и вычисление их произвдения.
# my_list_length = len(my_list)
# for i in range(my_list_length):
#     if i <= my_list_length / 2:
#         product = my_list[i] * my_list[my_list_length - 1 - i]
#         prod_list.append(product)
# print(f'Произведения крайних пар: {prod_list}.')
# print()
