# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

x = int(input("Enter X = "))
y = int(input("Enter Y = "))

if (x == 0 ):
    print("The point lies on the y-axis")
elif (y == 0):
    print("The point lies on the x-axis")
elif (x > 0 and y > 0):
    print ("The point lies in the 1 quadrant")
elif (x < 0 and y > 0):
    print ("The point lies in the 2 quadrant")
elif (x < 0 and y < 0):
    print ("The point lies in the 3 quadrant")
elif (x > 0 and y < 0):
    print ("The point lies in the 4 quadrant")