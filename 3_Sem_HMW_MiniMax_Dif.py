# Задача № 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print()
import random
my_list = []                      # Инициализация списка.
for _ in range(10):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), index))
print(f'Исходный список: {my_list}.')
   
float_list = []
for i in my_list:
    if float(i) != int(float(i)): # Исключим из рассчетов целые числа. 
        float_list.append(float(i))
print(f'Список вещественных чисел: {float_list}.')         

factorial_list = []
for i in float_list:              # Выделим числа после десятичной точки. 
    i = round(i - int(i), 3)
    factorial_list.append(i)
print(f'Список дробных частей:     {factorial_list}.')

max = factorial_list[0]
min = factorial_list[0]
for i in factorial_list:          # Найдем максимальное и минимальное значение среди
    if i > max:                   # дробных частей и вычислим их разность. 
        max = i
    elif i < min:
        min = i
print(f'max = {max}, min = {min}.')
result = round((max - min), 3)
print(f'max - min = {result}.')   # Печать результата. 
