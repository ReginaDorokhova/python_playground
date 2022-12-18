
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter the numder of the day of the week: '))
if (day > 7 or day < 0):
    print("Invalid day's number")
elif (day > 5):
    print("It is weekend!")
else:
    print("It is working day")

