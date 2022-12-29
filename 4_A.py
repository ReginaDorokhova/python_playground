# Задана натуральная степень k. Сформировать случайным образом список
#  коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

def getPowerCode(power):
    code = ''
    match power:
        case 0:
            code = u"\u2070"
        case 1:
            code = u"\u00B9"           
        case 2:
            code = u"\u00B2"
        case 3:
            code = u"\u00B3"
        case 4:
            code = u"\u2074"
        case 5:
            code = u"\u2075"
        case 6:
            code = u"\u2076"
        case 7:
            code = u"\u2077"
        case 8:
            code = u"\u2078"
        case 9:
            code = u"\u2079"
        case _:
            print("The power is incorrect")
    return code

def writePowerString(data, power):
    if (power > 1):
        for c in str(power):
            data.write(getPowerCode(int(c)))
    return


k = int(input("Enter the natural number k:"))
if k > 0:
    randomlist = []
    for i in range(0,k + 1):
        n = random.randint(0,100)
        randomlist.append(n)
    with open('file.txt', 'w') as data:
        i = len(randomlist) - 1
        hasData = False
        while i >= 0:
            if randomlist[i] > 0:
                if hasData:
                    data.write(" + ")
                if randomlist[i] >= 1 and i > 0:
                    data.write(str(randomlist[i]) + "*x")
                elif i == 0:
                    data.write(str(randomlist[i]))
                if i>1:
                    writePowerString(data, i)
                hasData = True
            i = i - 1
        data.write(" = 0")
    data.close()
else:
    print("k should be positive number")   

