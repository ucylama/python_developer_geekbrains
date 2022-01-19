stop_world = ''
sum_num = 0
error_num = []

print('Для завершения программы введите "end"')
while stop_world != 'end':
    num_user = input('\nВведите числа черед пробел и нажмите Enter: ').split()
    for i in num_user:
        try:
            if i == 'end':
                stop_world = 'end'
                continue
            sum_num += int(i)
        except ValueError:
            error_num.append(i)

    print(f'\nСумма введенных чисел: {sum_num}')
    print('Ошибочные значения были пропущены : ', *set(error_num))
