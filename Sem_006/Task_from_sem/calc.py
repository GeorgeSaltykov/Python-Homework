def over_calc(f, x, y):
    return f(x, y)


sum = lambda x, y: x + y
sub = lambda x, y: x - y
mult = lambda x, y: x * y
div = lambda x, y: x / y


def divs(dig, sym):
    dig[sym.index('/')] = over_calc(div, float(dig[sym.index('/')]),
                                    float(dig[sym.index('/') + 1]))
    dig.pop(sym.index('/') + 1)
    sym.pop(sym.index('/'))


def mults(dig, sym):
    dig[sym.index('*')] = over_calc(mult, float(dig[sym.index('*')]),
                                    float(dig[sym.index('*') + 1]))
    dig.pop(sym.index('*') + 1)
    sym.pop(sym.index('*'))


def sums(dig, sym):
    dig[sym.index('+')] = over_calc(sum, float(dig[sym.index('+')]),
                                    float(dig[sym.index('+') + 1]))
    dig.pop(sym.index('+') + 1)
    sym.pop(sym.index('+'))


def subs(dig, sym):
    dig[sym.index('-')] = over_calc(sub, float(dig[sym.index('-')]),
                                    float(dig[sym.index('-') + 1]))
    dig.pop(sym.index('-') + 1)
    sym.pop(sym.index('-'))
