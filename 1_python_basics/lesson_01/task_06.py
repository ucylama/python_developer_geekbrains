count_km = int(input('Введите текущее количество километров: '))
stop_km = int(input('Введите целевое количество километров: '))

days = 0

print('\nРезультаты:')
while count_km < stop_km:
    days += 1
    print(f'{days}-й день: {round(count_km, 2)}')
    count_km += (count_km * 0.1)
days += 1
print(f'{days}-й день: {round(count_km, 2)}')

print(f'На {days}-й день спортсмен достиг результата — не менее {stop_km} км.')
