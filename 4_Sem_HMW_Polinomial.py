# Задача A.	Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 
# или 10*x² = 0

print()
while True:       # Исключение некорректных условий ввода данных пользователем.            
    try:
        degree = int(input('Введите целое число D > 0: '))
        if degree < 0:
            print(f'Число {degree} < 0.')
        elif degree > 0:
            break
    except:
        print("Введите целое число D > 0.")

my_list = []      # Инициализация списка чисел в диапазоне [0, 100].
for i in range(0, 101):
    my_list.append(i)

import random
coef_nums = degree + 1           # Выделение нужного количества случайных чисел из списка.
coefs_list = random.sample(my_list, coef_nums)
if coefs_list[0] == 0 or coefs_list[0] == 1:                       
    coefs_list[0] = random.randint(1, 101)
print(f'Сгенерированный   список  коэффициентов: {coefs_list}.')

elems = []
def strL(coefs_lists, degree):        # Используем метод, чтобы получить,   
    for i in range(len(coefs_list)):  # левую часть многочлена в степени k.
        if degree - i > 1:
            if coefs_list[i] != 0:
                text = f'-{coefs_list[i]}*x**{degree - i}/'
            else:
                text = ''
        elif degree - i == 1:
            if coefs_list[i] != 0:
                text = f'-{coefs_list[i]}*x/'
            else:
                text = ''
        elif degree - i == 0:
            if coefs_list[i] != 0:
                text = f'-{coefs_list[i]}/'
            else:
                break
        elems.append(text) 
        strL = ''.join(elems)    
        strL = strL.replace('/-', ' + ').replace('-', '').replace('/', ' ')
    return strL
strL = strL(list, degree)

strR = '= 0'                         # Зададим правую часть многочлена.
def str_equation(str, strR):         # Используем функцию для объединения левой и   
    str_equation = strL + strR       # правой части многочлена.
    return str_equation
str_equation = str_equation(str, strR)
print(f'Многочлен степени {degree} имеет следующий вид: ')
print(str_equation)
print()

with open('new_file.txt', 'w') as data: # Запишем в файл полученный результат.
    data.write(f'If k = {degree}, then the polynomial is: {str_equation}.')