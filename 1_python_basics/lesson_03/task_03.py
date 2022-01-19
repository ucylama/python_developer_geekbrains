def my_func(val_1=float, val_2=float, val_3=float):
    list_num = [val_1, val_2, val_3]
    list_num.remove(min(val_1, val_2, val_3))
    return sum(list_num)


print(my_func(1, 2, 8))
