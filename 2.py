# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_statement(x,y,z):
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z :", (not (x or y or z) == (not x and not y and not z)),
     " for X =", x, ", Y = ", y, ", Z = ", z)

for X in [True, False]:
        for Y in [True, False]:
            for Z in [True, False]:
                check_statement(X, Y, Z)
