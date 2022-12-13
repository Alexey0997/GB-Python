# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print("\n" * 4)    # Способ отчистки консоли.
print('При вводе координат точки укажите целые числа, не равные нулю.')
X = int(input('Введите координату Х: '))
Y = int(input('Введите координату Y: '))

if X > 0 and Y > 0:
    print(f'Первая четверть. Диапазон возможных координат Х(0, PositiveInfinity), Y(0, PositiveInfinity).')
if X < 0 and Y > 0:
    print(f'Вторая четверть. Диапазон возможных координат Х(NegativeInfinity, 0), Y(0, PositiveInfinity).')
if X < 0 and Y < 0:
    print(f'Третья четверть. Диапазон возможных координат Х(NegativeInfinity, 0), Y(NegativeInfinity, 0).')
if X > 0 and Y < 0:
    print(f'Четвертая четверть. Диапазон возможных координат Х(0, PositiveInfinity), Y(NegativeInfinity, 0).')
