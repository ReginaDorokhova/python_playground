#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input("Enter the k: "));
if k > 0:
    list = [1, 0, 1]
    if k>1:
        i = 2
        while (i < k+1):
            list.append(list[2*i-2] + list[2*i-3])
            list.insert(0,  list[1] - list[0])
            i = i + 1
    print("Result list:", list)
else:
    print("k should be positive")
