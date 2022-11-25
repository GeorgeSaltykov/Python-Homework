import csv


def showing(data):
    x = data.split()
    i = x[0]
    with open('employee_list.csv', encoding='utf-8') as book:
        reader = csv.DictReader(book)
        count = 1
        for row in reader:
            if int(i) == count:
                for j in range(len(x)):
                    if j > 0:
                        print(f'{row[x[j]]}')
            count += 1


def show_everything():
    with open('employee_list.csv', encoding='utf-8') as emp:
        reader = csv.DictReader(emp)
        for row in reader:
            print(row['фио'], row['номер'], row['должность'])


