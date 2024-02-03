#ЗАДАЧА 1:
# Написать программу для сбора данных о пользователе.
# В первой строке попросить пользователя ввести имя.
# Во второй строке попросить пользователя ввести фамилию.
# В третьей строке попросить пользователя ввести год рождения.

name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
year_of_age = int(input("Введите год вашего рождения: "))
age = str(2024 - year_of_age)
print(name + ' ' + surname + ',' + age)
# Вывод: OLesia Arkhishina,32

# Задача 2:
# Написать программу, которая считывает целое число. Программа должна вывести следующее и предыдущее целое число с пояснительным текстом.
first_number = int(input("Введите число: "))
last_number = first_number - 1
next_number = first_number + 1
print(f"Следующее за числом {first_number}: {next_number} \nДля числа {first_number} предыдущее число: {last_number}")
# Вывод:
# Следующее за числом 14: 15
# Для числа 14 предыдущее число: 13

# Задача 3
# Написать программу для пересчёта величины временного интервала, заданного в минутах, в величину, выраженную в часах и минутах.
minutes = int(input("Введите количество минут: "))
print(f"{minutes} мин - это {minutes // 60} часа {minutes % 60} минут")
# Вывод:
# 150 мин - это 2 часа 30 минут

#Задание 4
#Написать программу, в которой рассчитываются сумма и произведение цифр положительного трёхзначного числа.
numbers = int(input("Введите трехзначное число: "))
num_1 = numbers // 100 % 10
num_2 = (numbers - num_1) // 10 % 10
num_3 = numbers % 10
sum_of_digits = num_1 + num_2 + num_3
mult_of_digits = num_1 * num_2 * num_3
print(f"Сумма цифр {sum_of_digits}")
print(f"Произведение чисел {mult_of_digits}")

# Вывод:
# Сумма цифр 12
# Произведение чисел 64

# Задача 5
# Написать программу, преобразовывающую мили в километры.
int_miles = input("Введите целое количество миль: ")
float_miles = input("Введите количество миль после запятой: ")
mileage = float("{0}.{1}".format(int_miles, float_miles))
kilometers = mileage * 1.61
print(f"{mileage} миль = {kilometers: .1f} км")

# Вывод:
# 13.6 миль =  21.9 км