#Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
distance = ((x1-x2)**2 + ((y1-y2))**2)**0.5
distance = float('{:.2f}'.format(distance))
print("The distance between points: ", distance)