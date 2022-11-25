import csv


def showing(id, data):
    with open('employee_list.csv', encoding='utf-8') as book:
        reader = csv.reader(book)
        for row in reader:
            if id in row:
                print(f'{row[data]}')
