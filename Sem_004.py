# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

import math
user_number = input()
user_number = user_number.split('.')
print(round(math.pi, len(user_number[1])))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

user_number = int(input())
prime_factors = []
for i in range(1, 11):
    if user_number % i == 0:
        prime_factors.append(i)
print(prime_factors)

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

user_list = input().split()
result_list = []
for i in user_list:
    if i not in result_list:
        result_list.append(i)
print(result_list)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

user_number = int(input())
result = list((str(random.randint(0, 100)), '*x^', str(user_number)))
for i in range(random.randint(0, user_number + 1)):
    result += ' + ', str(random.randint(0, 100)), '*x^', str(random.randint(0, user_number)), ' + ', str(random.randint(0, 100))
else:
    result += ' = 0'
data = open('second_file.txt', 'w')
data.writelines(result)
data.close()
data = open('second_file.txt', 'r')
for line in data:
    print(line)
data.close()
