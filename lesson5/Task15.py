#Задание 3. Сформировать из введенного числа обратное по порядку входящих в него
#цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit

print('"Обратное" ему число:', n2)

def PrintReverseOrder(N):

    if (N <= 0):
        return;
    else:
        print(N, end=" ")

    PrintReverseOrder(N - 1)
N = 123;
PrintReverseOrder(N)
