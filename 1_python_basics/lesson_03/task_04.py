import sys


def my_func(x=float, y=int):
    # проверка x и y на корректность
    if x > 0 and y < 0:
        part = 1
        divider = 1
        while part <= abs(y):
            divider *= x
            part += 1
        result = 1 / divider
    else:
        print('\nОшибка: убедитесь, что x > 0 и y < 0')
        print(f'Вы ввели x = {x} и y = {y}')
        sys.exit(1)
    return result


def ask_user():
    ask = int(input('Хотите ввести свои числа? 1 — да, 0 — нет: '))
    if ask == 1:
        x, y = input('Введите числа x и y через пробел (x > 0 и y < 0): ').split()
    else:
        x = 2
        y = -3
    try:
        return float(x), float(y)
    except ValueError:
        print(f'Ошибка: вы ввели "{x}" и "{y}", а нужно два числа :)')
        sys.exit(2)


X, Y = ask_user()
print(f'\nРезультат возведения {X} в степень {Y} равен {my_func(X, Y)}')
print('Проверка: ответ верный' if my_func(X, Y) == X ** Y else 'Хм, это неверный ответ')
