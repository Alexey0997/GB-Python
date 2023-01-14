# Задача № 3.	Реализуйте RLE алгоритм: модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# ФУНКЦИЯ RLE-КОДИРОВАНИЯ.

def encoding(data):                         
    cod = ''
    previous_char = ''
    count = 1
    if not data: 
        return ''
    for char in data:                       # Если текущий элемент не равен предудущему,   
        if char != previous_char:           # то результат кодирования части строки 
            if previous_char:               # равен количеству предыдущих символов. 
                cod += str(count) + previous_char 
            count = 1                       # Сбрасываем счетчик до 1.
            previous_char = char            # Текущий символ становится "предыдущим".
        else:
            count += 1                      # Если символ равен предыдущему, то увел. счетчик.
    else:
        cod += str(count) + previous_char
        return cod                          # Вернем результат шифрования.          

# ФУНКЦИЯ RLE-РАСШИФРОВКИ.

def decoding(data):           
    decoded_value = ''
    count = ''
    for char in data:                       # Если символ является цифрой, то 
        if char.isdigit():                  # счетчику присвоим значение этого символа.
            count += char
        else:                               # Если символ - не цифра, то в результат 
            decoded_value += char * int(count) # расшифровки положим count символов.
            count = ''
    return decoded_value                    # Вернем результат расшифровки. 

# ЗАПРОС ДАННЫХ У ПОЛЬЗОВАТЕЛЯ И ЗАПУСК АЛГОРИТМА ВЕТВЛЕНИЯ (КОДИРОВАНИЕ/ДЕШИФРОВКА)

desision = int(input('\nДля кодирования введите 1, для расшифровки введите 2: '))
if desision == 1:
    encoding_data = input('Введите данные для RLE-кодирования: ')
    with open('encoding_data.txt', 'w') as data:      # Запишем в файл данные для кодирования.
        data.write(f'Data for encoding: {encoding_data}')

    encoded_value = encoding(encoding_data)
    print(f'Результат кодирования: {encoded_value}\n')
    with open('encoding_result.txt', 'w') as data:      # Запишем в файл результат кодированя. 
        data.write(f'Result of encoding: {encoded_value}')

else:
    decoding_data = input('Введите данные для RLE-расшифровки: ')
    with open('decoding_data.txt', 'w') as data:      # Запишем в файл данные для расшифровки.
        data.write(f'Data for decoding: {decoding_data}')
    
    decoded_value = decoding(decoding_data)
    print(f'Результат расшифровки: {decoded_value}\n')
    with open('decoding_result.txt', 'w') as data:    # Запишем в файл результат расшифровки. 
        data.write(f'Result of decoding: {decoded_value}')

