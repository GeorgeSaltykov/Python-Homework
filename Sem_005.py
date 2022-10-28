# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# user_text = input('Введите текст: ').split()
# words = 'абв'
# res = [i for i in user_text if words not in i]
# print(res)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# print('Давайте сыграем в игру!\n На столе лежит 2021 конфета. Играют два игрока, делая ход друг после друга.\n'
#       'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n'
#       'Все конфеты оппонента достаются сделавшему последний ход.')
# sweets = 2021
# count = 0
# stop = True
# while sweets > 0:
#     while sweets > 0:
#         if stop == False:
#             stop = True
#             break
#         first_user = int(input('Игрок 1. Сколько конфет вы возьмете? '))
#         if 0 < first_user < 29:
#             sweets -= first_user
#             count += 1
#             print('Конфет осталось: ', sweets)
#             break
#         else:
#             print('Вы ввели неподходящее число конфет')
#             stop = False
#             break
#     while sweets > 0:
#         if stop == False:
#             stop = True
#             break
#         second_user = int(input('Игрок 2. Сколько конфет вы возьмете? '))
#         if 0 < second_user < 29:
#             sweets -= second_user
#             count += 1
#             print('Конфет осталось: ', sweets)
#             break
#         else:
#             print('Вы ввели неподходящее число конфет')
#             stop = False
#             break
# if count % 2 == 0:
#     print('Победил второй игрок!')
# else:
#     print('Победил первый игрок')

# Создайте программу для игры в ""Крестики-нолики"".

print('Крестики-нолики! \n'
      'Для того чтобы поставить крестик или нолик введите цифру нужного поля \n'
      'Для завершения игры введите "0"')

dict = {1: '[1]', 2: '[2]', 3: '[3]', 4: '[4]', 5: '[5]', 6: '[6]', 7: '[7]', 8: '[8]', 9: '[9]'}
field_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 1
for i in range(3):
    for j in range(3):
        print(dict[count], end=' ')
        count += 1
    print()
end = True
stop = True
while end == True:
    while end == True:
        if stop == False:
            stop = True
            break
        first_player = int(input('Игрок 1 ходит: '))
        if first_player in field_numbers:
            dict[first_player] = '[X]'
            field_numbers.remove(first_player)
            count = 1
            for i in range(3):
                for j in range(3):
                    print(dict[count], end=' ')
                    count += 1
                print()
            break
        else:
            print('Вы ввели неподходящее число')
            stop = False
            break
    if ((dict[1] == '[X]' and dict[2] == '[X]' and dict[3] == '[X]') or (dict[4] == '[X]' and dict[5] == '[X]' and dict[6] == '[X]')
        or (dict[7] == '[X]' and dict[8] == '[X]' and dict[9] == '[X]') or (dict[1] == '[X]' and dict[5] == '[X]' and dict[9] == '[X]')
        or (dict[3] == '[X]' and dict[5] == '[X]' and dict[7] == '[X]') or (dict[1] == '[X]' and dict[4] == '[X]' and dict[7] == '[X]')
        or (dict[2] == '[X]' and dict[5] == '[X]' and dict[8] == '[X]') or (dict[3] == '[X]' and dict[6] == '[X]' and dict[9] == '[X]')):
        print('Игрок 1 победил')
        end = False
        stop = False
    while end == True:
        if stop == False:
            stop = True
            break
        second_player = int(input('Игрок 2 ходит: '))
        if second_player in field_numbers:
            dict[second_player] = '[O]'
            field_numbers.remove(second_player)
            count = 1
            for i in range(3):
                for j in range(3):
                    print(dict[count], end=' ')
                    count += 1
                print()
            break
        else:
            print('Вы ввели неподходящее число')
            stop = False
            break
    if (dict[1] == ('[O]' and dict[2] == '[O]' and dict[3] == '[O]') or (dict[4] == '[O]' and dict[5] == '[O]' and dict[6] == '[O]')
    or (dict[7] == '[O]' and dict[8] == '[O]' and dict[9] == '[O]') or (dict[1] == '[O]' and dict[5] == '[O]' and dict[9] == '[O]')
    or (dict[3] == '[O]' and dict[5] == '[O]' and dict[7] == '[O]') or (dict[1] == '[O]' and dict[4] == '[O]' and dict[7] == '[O]')
        or (dict[2] == '[O]' and dict[5] == '[O]' and dict[8] == '[O]') or (dict[3] == '[O]' and dict[6] == '[O]' and dict[9] == '[O]')):
        print('Игрок 2 победил')
        end = False