# 2_1
# Напишите программу, 
# которая принимает на вход вещественное число и показывает сумму его цифр.

num = input("Enter the number: ")
try:
    num = float(num)
    sum = 0
    for c in str(num):
        if c.isdigit():
            sum = sum + int(c, base = 10)
    print("The sum of the digits of ", num, "is ", sum)
except ValueError:
    print('The provided value is not a number')

