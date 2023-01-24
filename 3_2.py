#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# source_list = [2, 3, 4, 5, 6]
# result = []
# i = 0
# while (i < len(source_list)/2) :
#     result.append(source_list[i]*source_list[-i-1])
#     i = i + 1

# print("Source list: ", source_list)
# print("Result list: ", result)

source_list = [2, 3, 4, 5, 6]
result = [source_list[i]*source_list[-i-1] for i in range(0, len(source_list)//2 + (len(source_list)%2 > 0))]
print("Source list: ", source_list)
print("Result list: ", result)