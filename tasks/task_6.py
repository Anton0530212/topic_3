# Программа, которая запрашивает у пользователя два числа
# и выводит на экран остаток от деления первого числа на второе.
num_1: int = int(input('Введите первое число: '))
num_2: int = int(input('Введите второе число: '))

result = num_1 % num_2
print('Остаток от деления', num_1, 'на', num_2, 'равен', result)
