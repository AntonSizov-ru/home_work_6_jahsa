filename = 'lesson06_pi_million_digits.txt'
with open(filename) as file:
    lines = file.readlines()
pi = ''
for line in lines:
    pi += line
b_day = input('Введите ваш год рождения в формате XXXX.\n:').strip()
if b_day in pi:
    print('Ваш год рождения встречается в значении числа Пи.')
    index = pi.index(b_day)
    print(f'Индекс первого вхождения в файл - {index},\n'
          f'Ваш год рождения занимает позиции в текстовом файле с {index + 1} по {index + 4} символ.')
else:
    print('Поздравляем, Вы - уникум.\n Ваш год рождения не встречается в значении числа Пи!')
