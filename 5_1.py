#Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

MAX_IN_MOVE = 28

def botMove(remain) -> int:
    global MAX_IN_MOVE
    move = remain % (MAX_IN_MOVE + 1)
    if move == 0:
        move = random.randint(1, MAX_IN_MOVE)
    return move

def userMove(remain) -> int:
    global MAX_IN_MOVE
    move = 0
    max_possible = min(MAX_IN_MOVE, remain)
    while move < 1 or move > max_possible:
        move = int(input(username + " move: "))
        if move < 1 or move > max_possible:
            print("Error: you can take at least 1 candy and no more than ", max(MAX_IN_MOVE, remain))
    return move

def checkWinner(remain, isUserMove):
    if remain == 0 and isUserMove:
        print("Game ended. Congrutalatians! " + username + " winner")
    elif remain == 0 and not isUserMove:
        print("Game ended. Bot is winner.")

username = input("Enter your name: ")
num = random.randint(30, 100)
print("Total number of sweets:", num)
isUserMove = random.randint(0, 1)

while num > 0 :
    num_in_move = 0
    if isUserMove:
        num_in_move = userMove(num)
    else :
        num_in_move = botMove(num)
        print("Bot move :", num_in_move)
    num = num - num_in_move
    print("Remain(", num, ")")
    checkWinner(num, isUserMove)
    isUserMove = not isUserMove


