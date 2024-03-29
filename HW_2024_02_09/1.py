# Написать программу, которая подсчитывает сумму только положительных чисел.
# Три числа программа должна по очереди получить из пользовательского ввода (stdin — стандартный поток ввода).

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a < 0 and b > 0 and c > 0:
    sum = b + c
elif a > 0 and b < 0 and c > 0:
    sum = a + c
elif a > 0 and b > 0 and c < 0:
    sum = b + a
elif a < 0 and b < 0 and c > 0:
    sum = c
elif a > 0 and b < 0 and c < 0:
    sum = a
elif a < 0 and b > 0 and c < 0:
    sum = b
elif a > 0 and b > 0 and c > 0:
    sum = a + b + c
else: 
    print('Вы ввели все отрицательные числа')
print(f'Сумма положительных чисел из трех равна {sum}')

# Вывод:
# Введите первое число: 6
# Введите второе число: -5
# Введите третье число: 7
# Сумма положительных чисел из трех равна 13.0

# Введите первое число: -8
# Введите второе число: -6
# Введите третье число: 9
# Сумма положительных чисел из трех равна 9.0

# комментарий преподавателя:
# Можно обойтись гораздо меньшим количеством проверок.
# Например мы можем сразу задать переменную total, в которую будем складывать
# только при условии того что число положительно.
# Например так:
# number_1 = float(input())
# number_2 = float(input())
# number_3 = float(input())
# total = 0
# if number_1 > 0:
#     total += number_1
# if number_2 > 0:
#     total += number_2
# if number_3 > 0:
#     total += number_3
# if total.is_integer():
#     print(f"{total:.0f}")
# else:
#     print(total) 
#
# PS: лучше не называть переменную sum, так как в python есть встроенная функция sum(), таким образом вы просто перезатёрли эту функцию