# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}

# import math
# user_number = input()
# user_number = user_number.split('.')
# print(round(math.pi, len(user_number[1])))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

user_number = int(input())
prime_factors = []
for i in range(1, 11):
    if user_number % i == 0:
        prime_factors.append(i)
print(prime_factors)

