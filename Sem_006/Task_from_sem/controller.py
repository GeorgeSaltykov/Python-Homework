import calc
import metamorf as meta
import user_interface as ui

digits = meta.morf_digit(ui.x)
symbols = meta.morf_symbols(ui.x)


def control():
    for _ in range(len(symbols)):
        if '/' in symbols and '*' in symbols:
            if symbols.index('/') < symbols.index('*'):
                calc.divs(digits, symbols)
            else:
                calc.mults(digits, symbols)
        if '/' in symbols and '*' not in symbols:
            calc.divs(digits, symbols)
        elif '*' in symbols and '/' not in symbols:
            calc.mults(digits, symbols)

    for _ in range(len(symbols)):
        if '+' in symbols and '-' in symbols:
            if symbols.index('-') < symbols.index('+'):
                calc.subs(digits, symbols)
            else:
                calc.sums(digits, symbols)
        if '+' in symbols and '-' not in symbols:
            calc.sums(digits, symbols)
        elif '-' in symbols and '+' not in symbols:
            calc.subs(digits, symbols)
    result = digits[0]
    return result
