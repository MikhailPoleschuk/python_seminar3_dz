# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input("-->"))
list1_ = [0, 1]
for i in range(2, n+1):
    number = int(list1_[i-2])+int(list1_[i-1])
    list1_.append(number)
list2_ = []
for i in range(1, len(list1_)):
    if i % 2 == 0:
        num_ = -int(list1_[i])
    else:
        num_ = int(list1_[i])
    list2_.append(num_)

print(list2_[::-1]+list1_)
