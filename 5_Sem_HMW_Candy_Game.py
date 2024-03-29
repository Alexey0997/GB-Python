# Задача № 1.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

print('\nУважаемый игрок, умный бот предлагает Вам принять участие \
в розыгрыше 150 конфет!\nПервый ход определяется жеребьевкой. \
За один ход можно забрать не более чем 28 конфет. \
\nВсе конфеты оппонента достаются игроку, сделавшему последний ход.\n')

import random               # Жеребьевка пользователя и бота. Кто введет большее число,    
while True:                 # тому принадлежит право первого хода.         
    lot1 = int(input('Введите число от 1 до 100 для жеребьевки: '))
    lot2 = random.randint(0, 101)
    try:
        if lot1 > lot2:
            print(f'Бот загадал {lot2}. Вы делаете первый ход.\n')
            break
        elif lot1 == lot2:
            print(f'Бот тоже загадал {lot2}. Жеребьевка будет продолжена.')
        elif lot1 < lot2:
            print(f'Бот загадал {lot2} и делает первый ход.\n')
            break
    except: 
        print('Проверьте правильность ввода данных.')


# ПРОВЕРКА ПРАВИЛЬНОСТИ ВВОДА ДАННЫХ ПОЛЬЗОВАТЕЛЕМ
max = 28                      # Макс. число конфет, которое можно взять за один ход.
min = 1                       # Мин.  число конфет, которое можно взять за один ход. 
def input_number(max, min):
    gamer_step = int(input(f'Ведите количество конфет от 1 до 28, которое хотите взять: '))
    while gamer_step < min or gamer_step > max:
        print(f'Вы хотите взять {gamer_step}.\
        \nПо правилам игры можно брать не менее 1 и не более 28 конфет.')
        gamer_step = int(
            input(f'Ведите количество конфет от 1 до 28, которое хотите взять: '))
    return gamer_step



# ИГРА 
candy_sum = 150                                 # Общее количество конфет.
def geming(candy_sum, max, min, lot1, lot2):
    if lot1 > lot2:                             # Первый ход делает пользователь.
        while candy_sum >= 0:
            gamer_step = input_number(max, min) # Вызов функции проверки корректности
            candy_sum -= gamer_step             # ввода данных пользователем.
            if candy_sum > 0:
                print(f'На столе осталось {candy_sum} конфет. Следующий ход бота.')
            else: 
                print(f'Конфет больше нет. Ура!!! Вы победили!')
                break
            if candy_sum > max:                 # Ход бота, если конфет > 28.
                bot_step = candy_sum%(max + 1)          
                candy_sum -= bot_step
                print(f'Бот взял {bot_step}. Осталось {candy_sum}\n')
            elif candy_sum >= min and candy_sum <= max:
                bot_step = candy_sum            # Ход бота, если конфет < 28.
                candy_sum -= bot_step
                print(f'Бот взял {bot_step}. Конфет не осталось и бот победил. Хотите поиграть еще?')
                break
    elif lot1 < lot2:                           # Если первый ход делает бот.
        while candy_sum >= 0:
            if candy_sum > max:                 # Ход бота, если конфет > 28.
                bot_step = candy_sum%(max + 1)           
                candy_sum -= bot_step
                print(f'Бот взял {bot_step}. Осталось {candy_sum}.')
            elif candy_sum >= min and candy_sum <= max:
                bot_step = candy_sum            # Ход бота, если конфет < 28.    
                candy_sum -= bot_step
                print(f'Бот взял {bot_step}. Конфет не осталось и бот победил. Хотите поиграть еще?')
                break        
            gamer_step = input_number(max, min) # Переход хода к пользователю.
            candy_sum -= gamer_step
            if candy_sum > 0:
                print(f'На столе осталось {candy_sum} конфет. Следующий ход бота.\n')
            else: 
                print(f'Конфет больше нет. Ура!!! Вы победили!')
                break

result = geming(candy_sum, max, min, lot1, lot2) # Вызов функции "ИГРА", печать результата.
print(result)
