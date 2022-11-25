import csv
def user_choice():
    choice = input('Для записи в список введите "w", для чтения отдельных элементов введите "id" и искомый столбец, \n'
                   'для просмотра всего списка введите "all", для выхода нажмите "q": ')
    return choice


def file_contains():
    with open('employee_list.csv', 'r', encoding='utf-8') as emp:
        reader = csv.reader(emp)
        count = True
        for row in reader:
            if count is True:
                print(f'Список содержит столбцы: {", ".join(row)}')
                count = False


def answer():
    data = input('Введите фамилию, имя, номер телефона и описание через пробел: ')
    return data
