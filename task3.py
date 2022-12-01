# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

list_ = [1.1, 1.2, 3.1, 10.01]


def max_number(any_list=None):
    if any_list is None:
        return print("передан пустой список, проверьте код")
    max_ = 0
    for i in range(len(any_list)):

        number = float(any_list[i]) % 1
       
        if number > max_:
            max_ = float(any_list[i]) % 1
            
    return round(max_,7)


def min_number(any_list=None):
    if any_list is None:
        return print("передан пустой список, проверьте код")
    min_ = float(any_list[0]) % 1
    for i in range(len(any_list)):

        number = float(any_list[i]) % 1
       
        if number < min_:
            min_ = float(any_list[i]) % 1
            
    return round(min_,7)


print(max_number(list_)-min_number(list_))

