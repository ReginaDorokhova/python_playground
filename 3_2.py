#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

list = [2, 3, 4, 5, 6]
result = []
i = 0
while (i < len(list)/2) :
    result.append(list[i]*list[-i-1])
    i = i + 1

print("Source list: ", list)
print("Result list: ", result)