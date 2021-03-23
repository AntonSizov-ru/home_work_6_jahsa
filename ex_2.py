import codecs as c

book = c.open('lesson06_cats_of_ulthar.txt', "r", "utf_8_sig")
text = book.read()
search_word = input('Введите слово для поска по тексту\n:').strip().lower()
count = len([word for word in text.lower().split() if word == search_word])
print(f'Слово {search_word} встречается в тексте {count} раз.\n')
i = len(text.lower().split(search_word))-1
print(f'Конструкция из слова {search_word} встречается в тексте {i} раз.\n')

strs = list(text.split('. '))
print(f'Строки содржащие в себе слово {search_word}:\n')
for line in strs:
    if search_word in line:
        print(line + '.')
