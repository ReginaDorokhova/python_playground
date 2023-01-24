#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

# source_list = [2, 3, 5, 9, 3]
# i = 1
# summa = 0
# while i < len(source_list) - 1:
#     summa = summa + source_list[i]
#     i = i + 2
# print("Source list: ", source_list)
# print("Sum: ", summa)

source_list = [2, 3, 5, 9, 3]
odd_ind_list = [source_list[i] for i in range(1, len(source_list), 2)]
print("Source list: ", source_list)
print("Sum: ", sum(odd_ind_list))