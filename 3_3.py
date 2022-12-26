#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов, отличной от 0.

list = [1.1, 1.2, 3.1, 5, 10.01] 

min = 0
max = 0
for i in range(0, len(list)):
    frac = list[i]%1
    if (frac > 0):
        frac = round(frac, len(str(list[i]).split(".")[1]))
        if (frac < min or min == 0):
            min = frac
        elif (frac > max):
            max = frac
print("Source list:", list)
print("max - min = ", max-min)


    