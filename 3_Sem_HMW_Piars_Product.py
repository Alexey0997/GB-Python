# Задача № 2.	Напишите программу, которая найдёт произведение пар чисел 
# списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

print('\n')                               # Инициализация списка.
my_list = []
for i in range(0, 20, 3):
    my_list.append(i)
print(f'Сгенерированный список:   {my_list}.')

product = 0                               # Определение пар крайних чисел 
prod_list = []                            # и вычисление их произвдения.
my_list_length = len(my_list)
for i in range(my_list_length):
    if i <= my_list_length / 2:
        product = my_list[i] * my_list[my_list_length - 1 - i]
        prod_list.append(product)
print(f'Произведения крайних пар: {prod_list}.')
print()