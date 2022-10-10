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
disjunction_1 = []
disjunction_2 = []
inversion_1 = []
inversion_x = []
inversion_y = []
inversion_z = []
conjunction_1 = []
conjunction_2 = []

def disjunction(a, b, c):
    for i in range(8):
        if a[i] == 1 or b[i] == 1:
            c.append(1)
        else:
            c.append(0)

def inversion(a, c):
    for i in range(8):
        c.append(-a[i])

def conjunction(a, b, c):
    for i in range(8):
        if a[i] == 1 and b[i] == 1:
            c.append(1)
        else:
            c.append(0)

inversion(disjunction(disjunction(x, y, disjunction_1), z, disjunction_2), inversion_1)
conjunction(conjunction(inversion(x, inversion_x), inversion(y, inversion_y), conjunction_1), inversion(z, inversion_z), conjunction_2)

if conjunction_2 == inversion_1:
    print('Yes')
else:
    print('No')