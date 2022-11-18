import csv


def writing(data):
    with open('phone_book.csv', 'a', encoding='utf-8') as book:
        writer = csv.writer(book)
        writer.writerow(data.split())
        print(data, 'успешно записано')
