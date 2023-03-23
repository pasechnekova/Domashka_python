# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
n = int(input('Введите число n: '))
print(f'{n+(int(str(n)+str(n))+(int(str(n)+str(n)+str(n))))}')