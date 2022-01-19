import sys

try:
    number_a, number_b = map(float, input('Введите два числа через пробел: ').split())
except ValueError as v:
    print(f'\nКажется это было не число:\n{v}\nПопробуйте снова')
    sys.exit(1)


def del_two_number(number_one, number_two):
    try:
        result = number_one / number_two
    except ZeroDivisionError:
        print('На ноль делить нельзя, повторите ввод чисел')
        sys.exit(2)
    return result


print(del_two_number(number_a, number_b))
