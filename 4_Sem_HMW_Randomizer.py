# НАПИСАТЬ СВОЙ РАНДОМАЙЗЕР (НЕ ИСПОЛЬЗОВАТЬ БИБЛИОТЕКУ RANDOM)

print('\n')               # Генерация положительных значений методом Фибоначи.
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):     # Генерация отрицательных значений с помощью Негафибоначчи. 
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        fib1 = 1
        fib2 = -1
        for i in range(2, n):
            fib1, fib2 = fib2, fib1 - fib2
        return fib2

while True:               # Исключение некорректных условий ввода данных пользователем.            
    numberMin = int(input('Введите минимальное  число Nmin > -100: '))
    try:
        if numberMin >= -11:
            numberMin = numberMin
            break
        elif numberMin < - 12 and numberMin >= -100:
            numberMin = -11
            break
    except: 
            print('Число {numberMin} < - 100. Введите число Nmin > -100: ')

while True:                # Исключение некорректных условий ввода данных пользователем. 
    try:
        numberMax = int(input('Введите максимальное число Nmax <  100: '))    
        if numberMax <= 11:
            numberMax = numberMax 
            break
        elif numberMax > 12 and numberMax <= 100:
            numberMax = 11
            break
    except:
        print('Число {numberMax} > 100. Введите число Nmax < 100: ')

if numberMin < - 12 :
    numberMin = -11
fib_list = [0]            # Инициализация списка, состоящего из данных двух методов.
for e in range(1, numberMax + 1):          # Сформируем общий список из двух методов.
    fib_list.append(Fibonacci(e))
    fib_list.insert(0, NegaFibonacci(e))

range_list = []                            # Из последовательности Фибоначчи выделим
for i in range(len(fib_list)):             # числа, попадающие в заданный диапазон.
    if fib_list[i] >= numberMin and fib_list[i] <= numberMax:
        range_list.append(fib_list[i])
print(f'Сгенерирован следующий числовой ряд: {range_list}.')
print()