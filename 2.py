# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_statement(x,y,z):
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z :", (not (x or y or z) == (not x and not y and not z)),
     " for X =", x, ", Y = ", y, ", Z = ", z)

check_statement(1, 0, 0)
check_statement(1, 1, 1)
check_statement(1, 0, 1)
check_statement(1, 1, 0)
check_statement(0, 0, 0)
check_statement(0, 1, 1)
check_statement(0, 0, 1)
check_statement(0, 1, 0)