#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите
#прибыль фирмы в расчете на одного сотрудника.
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
staff = int(input('Введите численность сотрудников фирмы: '))
bacon = revenue - costs
if bacon == 0: print('Выручка равна издержкам')
elif revenue > costs:
    print(f'Прибыль в этом месяце составила: {bacon}')
    profit = bacon/revenue
    print(f'Рентабельность выручки составила: {profit}')
    bacon_staff = float(bacon/staff)
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет = {bacon_staff}')
else:
    print('Организация убыточна')