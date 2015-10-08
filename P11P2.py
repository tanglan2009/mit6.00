# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6:30'
#         print self.time
#
# clock = Clock('5:30')
# clock.print_time()

# 5:30 prints out because we printed out the attribute self.time, not the
# local variable time.

#
# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print time
#
# clock = Clock('5:30')
# clock.print_time('10:30')

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

# boston_clock and paris_clock are two names for the same object.










