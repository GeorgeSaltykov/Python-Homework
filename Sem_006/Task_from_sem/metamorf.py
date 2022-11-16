import re


def morf_digit(data):
    return re.split('-|[*]|[+]|/', data)


def morf_symbols(data):
    symbols = []
    for i in data:
        if not i.isdigit():
            symbols.append(i)
    return symbols
