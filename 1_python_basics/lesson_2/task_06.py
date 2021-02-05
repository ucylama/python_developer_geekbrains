import sys

products_database = []
new_products = {'наименование': '',
                'стоимость': '',
                'количество': '',
                'единица измерения': ''}
all_products = {'наименование': [],
                'стоимость': [],
                'количество': [],
                'единица измерения': []}
num = 0

while True:
    if input('Начать ввод данных? да/нет: ').lower() == 'нет':
        print(f'Количество товаров в базе: {num}')
        break
    num += 1
    # input of data
    for key in all_products.keys():
        touch_values = input(f'{key} товара: ')
        try:
            new_products[key] = float(touch_values) \
                if (key == 'стоимость' or key == 'количество') \
                else touch_values
        except ValueError as v:
            print(f'\nВы ввели некорректные данные: \n{v} \nНачните заново')
            sys.exit(1)
        all_products[key].append(new_products[key])
    products_database.append((num, new_products.copy()))

    # statistics
    print('\nДобавленные товары: ')
    for key, values in all_products.items():
        print(f'{key}: {values}')
