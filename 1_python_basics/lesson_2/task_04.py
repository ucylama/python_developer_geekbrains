def word_to_line():
    j = 1
    for i in input('Крик души: ').split():
        print(f'{j}-я строка: {i[:10]}')
        j += 1


word_to_line()
