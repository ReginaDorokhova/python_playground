#Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Enter the quadrant number:"))
match quarter:
    case 1:
        print("X > 0, Y > 0")
    case 2:
        print("X < 0, Y > 0")
    case 3:
        print("X < 0, Y < 0")
    case 4:
        print("X > 0, Y < 0")
    case _:
        print("The quadrant numper incorrect")
