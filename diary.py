import codecs as c

diary = c.open('diary.txt', 'a+', 'utf_8_sig')
date = input('Введите дату записи\n:')
data = input('Введите запись для дневника\n:')
diary.write(f'{date}\n {data}\n')
output = input('Вы хотите прочитать дневник?\n ДА/НЕТ:').upper().strip()
if output == 'ДА':
    content = open('diary.txt')
    print(data)
    diary.close()
else:
    print('До новых встреч!')
    diary.close()
