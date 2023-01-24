# Задайте список из n чисел последовательности (1 + 1/n)^n, 
# выведеите его на экран, а так же сумму элементов списка.

# n = int(input("Enter n: "))
# if (n > 0):
#     list = []
#     sum = 0
#     for i in range(1, n+1):
#         x = float('{:.2f}'.format((1 + 1/i)**i))
#         sum = sum + x
#         list.append(x)
#     print(list)
#     print("Sum = ", sum)
# else:
#     print("Invalid n value")

import math
n = int(input("Enter n: "))
if (n > 0):
    list = [ float('{:.2f}'.format((1 + 1/i)**i)) for i in range(1, n+1)]
    print(list)
    print("Sum =", math.fsum(list))
else:
    print("Invalid n value")