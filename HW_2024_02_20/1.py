# Написать программу, которая принимает пользовательский ввод только до тех пор пока он соответствует условию.
# Программе в цикле получает из стандартного потока ввода (stdin) по одному целому числу, кратному семи. 
# При появлении любого числа, не делящегося на семь, цикл прерывается. 
# После окончания цикла программа выводит в stdout в одну строку все числа кратные семи в обратном порядке.

numbers = []
while True:
    n = int(input('Введите число: '))
    if n % 7 == 0:
        numbers.append(n)
    else:
        print(' '.join(map(str, reversed(numbers))))
        break
    

# Вывод:
# Введите число: 49
# Введите число: 21 
# Введите число: 14
# Введите число: 7
# Введите число: 56
# Введите число: 38
# 56 7 14 21 49