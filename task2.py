# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def input_list_number():
    len_ = int(input('введите длинну списка:'))
    new_list = []
    for i in range(len_):
        item_ = int(input("введите элемент:"))
        new_list.append(int(item_))
    return new_list


def func_summ_par(list_=None):
    if list_ is None:
        list_ = []
    result_list = []
    print(len(list_))
    if len(list_) % 2 > 0:
        len_ = len(list_) // 2 + 1
    else:
        len_ = len(list_) // 2
    count_len = len(list_)-1
    for item_ in range(len_):

        print(item_)
        sum_ = list_[item_] * list_[count_len]
        result_list.append(sum_)
        count_len -= 1
    return result_list


new_list = [2, 3, 4, 5, 6]  # input_list_number()
print(new_list)
print(func_summ_par(new_list))
