class MinStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num=''):
        self.numbers.append(num)

    def result(self):
        if len(self.numbers) > 0:
            return min(self.numbers)
        else:
            return 'None'


class MaxStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num=''):
        self.numbers.append(num)

    def result(self):
        if len(self.numbers) > 0:
            return max(self.numbers)
        else:
            return 'None'


class AverageStat:
    def __init__(self):
        self.numbers = []

    def add_number(self, num=''):
        self.numbers.append(num)

    def result(self):
        if len(self.numbers) > 0:
            average = 0
            count = 0
            for i in self.numbers:
                average += i
                count += 1
            return average / count
        else:
            return 'None'
