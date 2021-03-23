import show_rating as sr


def to_search():
    print(f'Данная программа поможет Вам узнать средний рейтинг среди сериалов разного жанра в срезе '
          f'по кол-ву сериалов.\n'
          f'Введите "стоп", если не хотите больше пользоваться программой.')
    while True:
        chose = input('\nУкажите жанр сериала по которому Вам необходим срез\n:').lower().strip()
        if chose in sr.shows.values():
            print(sr.to_collection(chose))
        elif chose == 'стоп':
            print('\nВсегда рады помочь, до новых встреч!')
            break
        else:
            print('\nУ нас не нашлось такого жанра, попробуйте с другим.')


print(to_search())
