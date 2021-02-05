import sys

try:
    number = int(input('Введите натуральное число: '))
except ValueError as e:
    print('Вы ввели некорректниые данные, попробуйте еще раз')
    sys.exit(1)

rating = [7, 5, 3, 3, 2]

if number < 1:
    print('Это число не натуральное, попробуйте снова')
elif number == 1:
    rating.append(1)
else:
    for i in rating:
        if i >= number:
            continue
        else:
            rating.insert(rating.index(i), number)
            break

print(*rating, sep=', ')
