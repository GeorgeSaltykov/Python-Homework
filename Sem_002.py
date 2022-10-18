# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

user_number = input('Введите число: ')
result = 0
for i in range(len(user_number)):
    if i != user_number.find('.'):
        result += int(user_number[i])
print('Сумма цифр числа:', result)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

user_number = int(input('Введите число: '))
result = [1]
for i in range(1, user_number):
    result.append(result[i - 1] * (i + 1))
print(result)

# Задайте список из n чисел последовательности (1 + 1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 4: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44}
# сумма: 9.06

n = int(input('Введите число: '))
dictionary = {}
for i in range(1, n + 1):
    dictionary[i] = round(((1 + 1 / i) ** i), 2)
print(dictionary)
sum = 0
for i in range(1, n + 1):
    sum += dictionary[i]
print(sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

user_number = int(input('Введите число: '))
list_random = []
for _ in range(user_number):
    list_random.append(random.randint(-user_number, user_number))
print(list_random)
multiply = 1
with open('file.txt', 'r') as data:
    for line in data:
        multiply *= list_random[int(line)]
        print(int(line), ':', list_random[int(line)])
print('Произведение чисел под индексами из списка равно: ', multiply)

# Реализуйте алгоритм перемешивания списка.

user_number = int(input('Введите число: '))
list_of_numbers = []
for _ in range(user_number * 2 + 1):
    list_of_numbers.append(-user_number)
    user_number -= 1
print(list_of_numbers)
for i in range(int(len(list_of_numbers) / 2 + 1)):
    temporary = list_of_numbers[i]
    list_of_numbers[i] = list_of_numbers[-i]
    list_of_numbers[-i] = temporary
temporary = list_of_numbers[0]
list_of_numbers.remove(list_of_numbers[0])
list_of_numbers.append(temporary)
print(list_of_numbers)

# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

first_list = [1, 2, 3, 2, 0]
second_list = [5, 1, 2, 7, 3, 2]
intersection = []
for i in first_list:
    for j in second_list:
        if j == i:
            intersection.append(j)
            break
print(intersection)
