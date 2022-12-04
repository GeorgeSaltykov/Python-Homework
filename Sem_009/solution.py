class TicTacToeBoard:
    def __init__(self):
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.player = True
        self.result = False

    def new_game(self):
        self.field = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.player = True
        self.result = False
        print('Новая игра!', end='\n')
        self.get_field()

    def get_field(self):
        for i in self.field:
            print(i)

    def check_line(self, x, y, z, symbol):
        if x == symbol and y == symbol and z == symbol:
            self.result = True

    def check_field(self, symbol):
        count = 0
        for i in range(3):
            self.check_line(self.field[i][0], self.field[i][1], self.field[i][2], symbol)
            self.check_line(self.field[0][i], self.field[1][i], self.field[2][i], symbol)
            for j in range(3):
                if self.field[i][j] == '-':
                    count += 1
        self.check_line(self.field[0][0], self.field[1][1], self.field[2][2], symbol)
        self.check_line(self.field[0][2], self.field[1][1], self.field[2][0], symbol)

        if self.result is True and symbol == 'X':
            return 'X'
        elif self.result is True and symbol == '0':
            return '0'
        elif self.result is False and count < 2:
            self.result = True
            return 'D'
        else:
            return ''

    def make_move(self, row, col):
        if self.field[row - 1][col - 1] == '-' and self.player is True:
            self.field[row - 1][col - 1] = 'X'
            if self.check_field('X') == 'X':
                print('Победил игрок X')
            elif self.check_field('X') == 'D':
                print('Ничья')
            else:
                print('Продолжаем играть')
            self.player = False
        elif self.field[row - 1][col - 1] == '-' and self.player is False:
            self.field[row - 1][col - 1] = '0'
            if self.check_field('0') == '0':
                print('Победил игрок 0')
            elif self.check_field('0') == 'D':
                print('Ничья')
            else:
                print('Продолжаем играть')
            self.player = True
        elif self.result is True:
            print('Игра уже завершена')
        else:
            print(f'Клетка {row}, {col} уже занята.')
