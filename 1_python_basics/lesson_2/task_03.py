import sys

try:
    number = int(input('Введите число от 1 до 12: '))
except ValueError as e:
    print('Вы ввели некорректниые данные, попробуйте еще раз')
    sys.exit(1)

dict_seasons = {
    'зима': [12, 1, 2],
    'весна': [3, 4, 5],
    'лето': [6, 7, 8],
    'осень': [9, 10, 11]
}

if 0 < number <= 12:
    for name, months in dict_seasons.items():
        if number in months:
            print(f'{number} — это {name}')
else:
    print(f'Вы ввели {number} — такого месяца не бывает :)')
