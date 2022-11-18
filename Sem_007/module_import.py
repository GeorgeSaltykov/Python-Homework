import csv


def showing(data):
    with open('phone_book.csv', encoding='utf-8') as book:
        reader = csv.reader(book)
        for row in reader:
            if data in row:
                print(row)
