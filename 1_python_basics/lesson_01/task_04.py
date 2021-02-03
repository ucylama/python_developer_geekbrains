user_input = int(input('Введите целое положительное число: '))

last_number = user_input % 10
number = user_input // 10

while number > 0:
    if number % 10 > last_number:
        last_number = number % 10
    number = number // 10

print(f'Наибольшая цифра в числе: {last_number}')
