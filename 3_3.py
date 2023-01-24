#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов, отличной от 0.

# source_list = [1.1, 1.2, 3.1, 5, 10.01] 

# minimum = 0
# maximum = 0
# for i in range(0, len(source_list)):
#     frac = source_list[i]%1
#     if (frac > 0):
#         frac = round(frac, len(str(source_list[i]).split(".")[1]))
#         if (frac < minimum or minimum == 0):
#             minimum = frac
#         elif (frac > maximum):
#             maximum = frac
# print("Source source_list:", source_list)
# print("maximum - minimum = ", maximum-minimum)

def getFrac(num):
    frac = num%1
    if (frac > 0):
        frac = round(frac, len(str(num).split(".")[1]))
    return frac

source_list = [1.1, 1.2, 3.1, 5, 10.01] 

frac_list = list(filter(lambda e : not e==0, map(getFrac, source_list)))
print(frac_list)
print("maximum - minimum = ", max(frac_list)-min(frac_list))

    