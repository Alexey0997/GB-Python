# Задача № 4.	Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

print('\n')
while True:                 # Исключение некорректных условий ввода данных пользователем.            
    try:
        decimal_num = int(input('Введите целое число N > 0: '))
        if decimal_num == 0:
            print('Десятичное число 0 = 0 в двоичной системе.')
        elif decimal_num > 0:
            break
    except:
        print("Введите целое число N > 0.")
        

nums = []                    # Построение списка из остатков от деления на 2.       
result = 0
i = decimal_num
while i >= 1:
    result = int(i%2)
    nums.append(result)
    i = i/2

def binary_num(nums):        # Используем метод для разворот списка 
    binary_list = []         # и трансформации его элементов в число.
    for i in reversed(nums):
        binary_list.append(i)
    binary_num = int(''.join(map(str, binary_list)))  
    return binary_num
binary_num = binary_num(nums)
print(f'Десятичное число {decimal_num} = {binary_num} в двоичной системе.')
print()