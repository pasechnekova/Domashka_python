#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введи число N:'))
i = 0
while 2 ** i <= n:
    print(f' 2 в степени {i} равна {2 ** i}')
    i += 1
