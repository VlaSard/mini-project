import cipher


def unpack(line):
    return ", ".join(map(str, line))


print('Добро пожаловать в программу Caesar.')

CAESAR = True

while CAESAR:

    # Режим работы: шифровать / дешифровать.
    repl = input('\nВыберите режим работы шифровать или дешифровать текст: '
                 '(по умолчанию шифровать) ')

    while True:

        encrypted = ['encrypt', 'e', 'шифровать', 'ш']
        decrypted = ['decrypt', 'd', 'дешифровать', 'д']

        if len(repl) == 0 or repl in encrypted:
            MODE = 1
            break

        if repl in decrypted:
            MODE = -1
            break

        repl = input(f'Необходимо ввести ([{unpack(encrypted)}]'
                     f' или [{unpack(decrypted)}]): ')

    # Направление кодировки.
    repl = input('\nВыберите направление кодировки вправо или влево:'
                 ' (по умолчанию вправо) ')

    while True:

        left = ['left', 'l', 'влево', 'л']
        right = ['right', 'r', 'вправо', 'п']

        if len(repl) == 0 or repl in right:
            ROUTE = 1
            break

        if repl in left:
            ROUTE = -1
            break

        repl = input(f'Необходимо ввести ([{unpack(left)}]'
                     f' или [{unpack(right)}]): ')

    # Определение ключа кодирования.
    KEY = input('\nВведите ключ (по умолчанию ключ равен длине слова): ')

    while True:

        if len(KEY) == 0 or KEY == '0':
            KEY = False
            break

        if KEY.isdigit():
            KEY = int(KEY) * ROUTE * MODE
            break

        KEY = input('Необходимо ввести число или нажать "Enter": ')

    # Получение текст для обработки.
    text_in = cipher.get_parse(input('\nВведите текст для кодировки:\n'))

    # Обработка текста.
    text_ou = []

    for word in text_in:

        if KEY is False:
            offset = len(word)

        else:
            offset = KEY

        text_ou.append(cipher.get_coder(word, offset))

    # Обработка текста завершена.
    print('\nИсходный текст успешно обработан:', ''.join(text_ou), sep='\n')

    # Запрос продолжения работы.
    repl = input('\nОбработать еще один текст?: (нет - по умолчанию) ')

    while True:

        yes = ['yes', 'y', 'да', 'д']
        no = ['no', 'n', 'нет', 'н']

        if len(repl) == 0 or repl in no:
            CAESAR = False
            break

        if repl in yes:
            CAESAR = True
            break

        repl = input(f'Необходимо ввести ([{unpack(yes)}]'
                     f' или [{unpack(no)}]): ')
