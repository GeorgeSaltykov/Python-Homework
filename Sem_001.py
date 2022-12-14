import math
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number_of_day = int(
    input('Введите число, обозначающее порядковый номер дня недели '))
if 8 > number_of_day > 5:
    print('Выходной день')
elif 6 > number_of_day > 0:
    print('Будний день')
else:
    print('Вы ввели неподходящее число')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = [0, 0, 0, 1, 0, 1, 1, 1]
y = [0, 0, 1, 0, 1, 1, 0, 1]
z = [0, 1, 0, 0, 1, 0, 1, 1]

l = len(x)

def disjunction(a, b):
    c = []
    for i in range(l):
        if a[i] == 1 or b[i] == 1:
            c.append(1)
        else:
            c.append(0)
    return c

def inversion(a):
    c = []
    for i in range(l):
        if a[i] == 1:
            c.append(0)
        elif a[i] == 0:
            c.append(1)
    return c

def conjunction(a, b):
    c = []
    for i in range(l):
        if a[i] == 1 and b[i] == 1:
            c.append(1)
        else:
            c.append(0)
    return c

if inversion(disjunction(disjunction(x, y), z)) == conjunction(conjunction(inversion(x), inversion(y)), inversion(z)):
    print('Yes')
else:
    print('No')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите х не равный нулю: '))
y = int(input('Введите y не равный нулю: '))

if x > 0 and y > 0:
    print('Точка находится в 1-ой четверти плоскости')
elif x < 0 and y > 0:
    print('Точка находится во 2-ой четверти плоскости')
elif x < 0 and y < 0:
    print('Точка находится в 3-ей четверти плоскости')
elif x > 0 and y < 0:
    print('Точка находится в 4-ой четверти плоскости')
else:
    print('Что-то пошло не так, попробуйте снова')

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти: '))

if quarter_number == 1:
    print('x = [1, 2, 3...)\ny = [1, 2, 3...)')
elif quarter_number == 2:
    print('x = [-1, -2, -3...)\ny = [1, 2, 3...)')
elif quarter_number == 3:
    print('x = [-1, -2, -3...)\ny = [-1, -2, -3...)')
elif quarter_number == 4:
    print('x = [1, 2, 3...)\ny = [-1, -2, -3...)')
else:
    print('Вы ввели некорректное число')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

A = list(map(int, input('Введите координаты точки A через запятую: ').split(',')))
B = list(map(int, input('Введите координаты точки B через запятую: ').split(',')))

print(round(math.sqrt((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2), 3))