# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# number_of_day = int(
#     input('Введите число, обозначающее порядковый номер дня недели '))
# if 8 > number_of_day > 5:
#     print('Выходной день')
# elif 6 > number_of_day > 0:
#     print('Будний день')
# else:
#     print('Вы ввели неподходящее число')

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

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
