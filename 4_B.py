# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import random

def generateKoefList():
    k = random.randint(1, 10)
    randomlist = []
    for i in range(0,k + 1):
        n = random.randint(0,100)
        randomlist.append(n)
    return randomlist

def writePolynomialInFile(koefList, path):
    with open(path, 'w') as data:
        i = len(list(koefList)) - 1
        hasData = False
        while i >= 0:
            if koefList[i] > 0:
                if hasData:
                    data.write(" + ")
                if koefList[i] >= 1 and i > 0:
                    data.write(str(koefList[i]) + "*x")
                elif i == 0:
                    data.write(str(koefList[i]))
                if i>1:
                    data.write("^" + str(i))
                hasData = True
            i = i - 1
        data.write(" = 0")
    data.close()
    return

def getDictFromFile(path):
    data = open(path,  mode = 'r')
    line = data.readline(); 
    list = line.split(" = ")[0].split(" + ")
    dictionary = {}
    for item in list:
        pair = item.split("*x")
        if len(pair) == 1:
            dictionary.update({0:int(pair[0])})
        elif not pair[1]:
            dictionary.update({1:int(pair[0])})
        else:
            n = int(pair[1].lstrip('^'))
            dictionary.update({n:int(pair[0])})
    data.close
    return dictionary


path1 = 'file1.txt'
writePolynomialInFile(generateKoefList(), path1)
dict1 = getDictFromFile(path1)

path2 = 'file2.txt'
writePolynomialInFile(generateKoefList(), path2)
dict2 = getDictFromFile(path2)

for power in dict1:
    if power in dict2:
        dict1[power] = dict1[power] + dict2.pop(power)
dict1.update(dict2)
dict1 = {k : dict1[k] for k in sorted(dict1, reverse=True)}
list = []
for key in dict1:
    if dict1[key] != 0:
        if dict != 1 or key == 0:
            converted = str(dict1[key])
        if key > 1:
            converted += "*x^" + str(key)
        elif key == 1:
            converted += "*x"
        list.append(converted)

    with open('file3.txt', 'w') as data:
        data.write(' + '.join(list))
        data.write(" = 0")
    data.close()


