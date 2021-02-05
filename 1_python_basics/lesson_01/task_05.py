revenue = float(input('Введите сумму выручки: '))
costs = float(input('Введите сумму издержек: '))

profit = revenue - costs # прибыль
profit_margin = profit / revenue # рентабельность выручки

if profit > 0:
    print('\nКомпания работает в прибыль\n')
    customer_cnt = int(input('Введите количество сотрудников в компании: '))
    print(f'\nРентабельность выручки: {profit_margin}',
          f'Прибыль компании на одного сотрудника: {profit / customer_cnt}',
          sep='\n')
elif profit < 0:
    print('\nКомпания работает в убыток')
else:
    print('\nКомпания работает "в ноль"')
