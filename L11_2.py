# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self):
#         time = '6:30'
#         print self.time
#
# clock = Clock('5:30')
# clock.print_time()
#

# class Clock(object):
#     def __init__(self, time):
#         self.time = time
#     def print_time(self, time):
#         print time
#
# clock = Clock('5:30')
# clock.print_time('10:30')


"""
Above code is confusing. It is less confusing if you give parameters, local
variables, and attributes different, distinct names to avoid the confusion that
arises in this problem.
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

"""
boston_clock and paris_clock are two names for the same object.
This is called aliasing.
"""






























