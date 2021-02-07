import sys


def print_user_info(first_name, last_name, birth_year, city_name, email, tel_number):
    print(first_name, last_name, birth_year, city_name, email, tel_number)


def user_info():
    """
    Функция запрашивает у пользователя данные для анкеты: имя, фамилия,
    дата рождения, город проживания, электронная почта, номер телефона
    :return: dict
    """
    about_user = {'имя': '', 'фамилия': '', 'дата рождения': '', 'город': '', 'эл.почта': '', 'телефон': ''}
    print('Заполните анкету:')
    for key in about_user.keys():
        input_info = input(f'— {key}: ')
        try:
            about_user[key] = int(input_info) if key == 'дата рождения' else input_info
        except ValueError as v:
            print('Вы ввели некорректную дату рождения')
            sys.exit(1)
    return about_user


# запросим данные у пользователя
f_name, l_name, birth, city, mail, tel = tuple(user_info().values())
# распечатаем полученные данные
print_user_info(f_name, l_name, birth, city, mail, tel)
