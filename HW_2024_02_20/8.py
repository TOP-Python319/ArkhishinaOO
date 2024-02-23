# Написать программу, которая требуемое количество чисел последовательности Фибоначчи.
# Программа получает из stdin натуральное число n. 
# Далее, программа считает и выводит в stdout n чисел последовательности Фибоначчи.

fib_num1 = fib_num2 = 1
 
n = int(input("Введите число: "))
 
print(fib_num1, fib_num2, end=' ')
 
for i in range(2, n):
    fib_num1, fib_num2 = fib_num2, fib_num1 + fib_num2
    print(fib_num2, end=' ')
    
    
# Вывод:
# Введите число: 1
# 1 1

# Введите число: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597