# Задача № 2.	Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом


board = list(range(1, 10))  # Используем список для заполнения игрового поля.

# ФУНКЦИЯ СОЗДАНИЯ ИГРОВОГО ПОЛЯ
def board_creation(board):       
    print ('=' * 15)        # Проведем верхнюю горизонтальную границу.
    for i in range(3):      # Обозначим вертикальные границы клеток и заполним их цифрами.
        print ('||', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '||')
        print ('=' * 15)    # Обозначим нижние горизонтальные границы каждого ряда. 


# ФУНКЦИЯ ВВОДА И ПРОВЕРКИ ДАННЫХ ПОЛЬЗОВАТЕЛЕМ
def take_input(player_token):
    valid = False
    while not valid:        # Задаем условия выхода из цикла.
        player_answer = input(f'Куда поставим {player_token}? ')
        try:                # Проверяем, ввел ли пользователь число или другой символ.
            player_answer = int(player_answer)
        except:             # Если введено не число, напоминаем правила.
            print ('Некорректный ввод данных. Введите число от 1 до 9.')
            continue        # Если число в диапозоне [0,9], то проверяем не занято ли поле
        if player_answer >= 1 and player_answer <= 9:       # символами X или O.
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True                     
            else:           # Если поле занято, сообщаем и предлагаем ввести номер  
                print ('Эта клетка уже занята.')            # свободного поля.
        else:
            print ('Некорректный ввод. Введите номер свободного поля от 1 до 9.')


# ФУНКЦИЯ ПРОВЕРКИ УСЛОВИЙ ВЫИГРЫША
def check_win(board):       # Выигрышные комбинации (вертикали, горизонтали, диаганали).
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:  # Если выигрышные поля заняты одинаковым символом, то 
        if board[each[0]] == board[each[1]] == board[each[2]]: # соответствующий игрок
            return board[each[0]]                              # одержал победу.
    return False

# ФУНКЦИЯ ПРОВЕДЕНИЯ ИГРЫ В КРЕСТИКИ-НОЛИКИ (ИСПОЛЬЗОВАНИЕ ПОЛЯ, ХОДОВ И ПРОВЕРКИ ПОБЕДЫ)
def main(board):
    counter = 0               # Для смены очередности ходов вводим счетчик.
    win = False
    while not win:
        board_creation(board)
        if counter % 2 == 0:  # Если счетчик имеет четное значение, то ходит 'X'.
            take_input('X')
        else:
            take_input('O')   # Если счетчик имеет нечетное значен, то ходит 'O'. 
        counter += 1
        if counter > 4:       # Если сделано более четырех ходов, то сравниваем текущее
            winer = check_win(board)               # положение с выигрышными комбинациями. 
            if winer:         # При совпадении текущей и выигрышной комбинаций сообщаем
                print (f'"{winer}" выиграл!') # о победе и прекращаем цикл.
                win = True
                break
        if counter == 9:      # Если все поля заполнены, но нет совпадений с выигрышными
            print ('Ничья!')  # комбинациями, то сообщаем о ничье и прекращаем цикл.
            break
    board_creation(board)

main(board)                   # Вызываем функцию игры в крестики-нолики. 