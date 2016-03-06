class Time(object):
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return  str(self.hours) + ':' + str(self.minutes) + ':' + str(self.seconds)

time = Time(11, 59, 30)
# time.hours = 11
# time.minutes = 59
# time.seconds = 30
print time
print isinstance(time, Time)

def add_time(t1, t2):

    hours = t1.hours + t2.hours
    minutes = t1.minutes + t2.minutes
    seconds = t1.seconds + t2.seconds
    sum = Time(hours, minutes, seconds)
    return sum

current_time = Time(9, 14, 30)
# current_time.hours = 9
# current_time.minutes = 14
# current_time.seconds = 30
bread_time = Time(3, 35, 0)
# bread_time.hours = 3
# bread_time.minutes = 35
# bread_time.seconds = 0
done_time = add_time(current_time, bread_time)
print done_time

#











