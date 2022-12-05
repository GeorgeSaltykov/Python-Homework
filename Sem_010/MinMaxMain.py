from MinMaxAverage import *

# пример 1

values = [1, 2, 4, 5]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# пример 2

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# print(mins.result(), maxs.result(), average.result())

# пример 3

# values = [1, 0, 0]
# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)
# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
