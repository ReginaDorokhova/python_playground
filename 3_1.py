#Задайте список из нескольких чисел. 
#Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

list = [2, 3, 5, 9, 3]
i = 1
sum = 0
while i < len(list) - 1:
    sum = sum + list[i]
    i = i + 2
print("Source list: ", list)
print("Sum: ", sum)