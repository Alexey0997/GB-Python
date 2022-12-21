# Задача № 5.	Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

print('\n')               # Рассчет элементов списка Фибоначчи с помощью рекурсии.
def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):     # Использование цикла для рассчета элементов Негафибоначчи. 
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

fib_list = [0]            # Инициализация списка, состоящего из данных двух методов.
number = int(input('Введите целое число: '))
for e in range(1, number + 1):
    fib_list.append(Fibonacci(e))
    fib_list.insert(0, NegaFibonacci(e))
print(f'Список Фибоначчи для числа {number}: {fib_list}.')
print()