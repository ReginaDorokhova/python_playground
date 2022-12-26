#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input("Enter the number:"))
bin = ''
 
while num > 0:
    bin = str(num % 2) + bin
    num = num // 2
 
print(bin)