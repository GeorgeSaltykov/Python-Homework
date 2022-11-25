import csv
import datetime as dt


def log(x):
    with open('logger.csv', 'a', encoding='utf-8') as logg:
        write = csv.writer(logg)
        if x is True:
            write.writerow(['Запись', dt.datetime.now()])
        else:
            write.writerow(['Чтение', dt.datetime.now()])

