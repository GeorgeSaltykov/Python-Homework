# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

user_list = list(map(int, input().split()))
amount = 0
for i in range(len(user_list)):
    if i % 2 != 0:
        amount += user_list[i]
print(amount)

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

user_list = list(map(int, input().split()))
multiply_list = []
index = -1
l = len(user_list) // 2
if len(user_list) % 2 != 0:
    l += 1
for i in range(l):
    multiply_list.append(user_list[i] * user_list[index])
    index -= 1
print(multiply_list)

# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

user_list = (input().split())
without_points = []
list_of_fractions = []
for i in range(len(user_list)):
    without_points.append(user_list[i].split('.'))
for i in range(len(without_points)):
    if len(without_points[i]) > 1:
        list_of_fractions.append(float('0.' + without_points[i][1]))
print(list_of_fractions)
print(max(list_of_fractions) - min(list_of_fractions))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

user_number = int(input())
binary = []
while user_number > 1:
    binary.insert(0, user_number % 2)
    user_number = int(user_number / 2)
if user_number == 1:
    binary.insert(0, 1)
print(binary)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

user_number = int(input())
fibonacci = [0, 1]
for i in range(2, user_number + 1):
    fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
for _ in range(user_number):
    i = 1
    fibonacci.insert(0, -(fibonacci[i - 1] - fibonacci[i]))
print(fibonacci)

