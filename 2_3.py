#Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int


from random import randrange

#Using known algorithm Sattolo

def sattoloCycle(list):
    i = len(list)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        list[j], list[i] = list[i], list[j]
    return

list = [1, 2, 3, 4, 5, 6]
print("Source list: ", list)
sattoloCycle(list)
print("Result list: ", list)