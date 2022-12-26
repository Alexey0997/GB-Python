# Задача B.	 Даны два файла, в каждом из которых находится запись многочлена. 
# Необходимо сформировать файл, содержащий сумму многочленов.

print()
polynomial1 = '4*x**2 + 6*x - 5'             # Инициализировать первый многочлен.
print(f'First  polynomal is: f(x) = {polynomial1}.')
with open('firstFile.txt', 'w') as data:     # Записать первый многочлен в файл № 1.
    data.write(f'First polynomal is: f1(x) = {polynomial1}')

polynomial2 = '-8*x**2 + 2'                  # Инициализировать второй многочлен.
print(f'Second polynomal is: f(x) = {polynomial2}.')
with open('secondFile.txt', 'w') as data:    # Записать второй многочлен в файл № 2.
    data.write(f'Second polynomal is: f2(x) = {polynomial2}')

f1 = []
path = 'firstFile.txt'                       # Считаем данный из файла № 1.
data = open(path, 'r')
for line in data:                            
    f1.append(line) 
    f1 = ''.join(f1)    
    f1 = f1.replace('First polynomal is: f1(x) =', '')
data.close()                                 

f2 = []
path = 'secondFile.txt'                      # Считаем данные из файла № 2.
data = open(path, 'r')
for line in data:                           
    f2.append(line) 
    f2 = ''.join(f2)    
    f2 = f2.replace('Second polynomal is: f2(x) =', '')
data.close()                                 

polySum = f1 + f2                            # Найдем сумму многочленов и
print(f'f1(x) + f2(x) = {polySum}')          # запишем ее в файл № 3.
with open('thirdFile.txt', 'w') as data:     
    data.write(f'f1(x) = {polynomial1}\n')
    data.write(f'f2(x) = {polynomial2}\n')
    data.write(f'The polynomals sum is: \n')
    data.write(f'f1 + f2 = {polySum}')
print()