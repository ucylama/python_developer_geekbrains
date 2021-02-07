def int_func(text=str):
    return text.capitalize()


user_list = input('Введите слова через пробел: ').split()
print(*list(int_func(i) for i in user_list))
