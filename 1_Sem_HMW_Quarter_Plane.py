# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print("\n" * 4)    # Способ отчистки консоли.
print('При вводе координат точки укажите целые числа, не равные нулю.')
X = int(input('Введите координату Х: '))
Y = int(input('Введите координату Y: '))

if X > 0 and Y > 0:
    print(f'Точка с координатами ({X}, {Y}) находится в первой четверти.')
if X < 0 and Y > 0:
    print(f'Точка с координатами ({X}, {Y}) находится во второй четверти.')
if X < 0 and Y < 0:
    print(f'Точка с координатами ({X}, {Y}) находится в третьей четверти.')
if X > 0 and Y < 0:
    print(f'Точка с координатами ({X}, {Y}) находится в четвертой четверти.')