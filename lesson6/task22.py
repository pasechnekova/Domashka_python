#2. Представлен список чисел. Необходимо вывести элементы исходного списка,
#значения которых больше предыдущего элемента.

result_list = []
list = [int(i) for i in input("Введите список чисел: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list)
print("Список, элементы которого больше предыдущего: ", result_list)