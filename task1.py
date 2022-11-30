# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12
def func_summ_nechet(list_=None):
    if list_ is None:
        list_ = []
    sum_ = 0
    for item_ in range(1, len(list_), 2):
        sum_ += list_[item_]

    return sum_


def input_list_number():
    len_ = int(input('введите длинну списка:'))
    new_list = []
    for i in range(len_):
        item_ = int(input("введите элемент:"))
        new_list.append(item_)
    return new_list

new_list=input_list_number()
print(new_list)
print(func_summ_nechet(new_list))
