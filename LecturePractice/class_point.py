# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x
#         self.y = y
#
#     def distance_from_origin(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#
#
# p = Point(3, 4)
# print p.x
# print p.y
#
# print p.distance_from_origin()
#
# q = Point(5, 12)
# print q.x
# print q.y
# print q.distance_from_origin()
#
# r = Point()
# print r.x
# print r.y
# print r.distance_from_origin()
#
# """
# When defining a method, the first parameter refers to the instance being created.
# It is customary to name this parameter self.
# In the example above, the self parameter refers to the instances p, q, and r respectively.
# """


class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((x ** 2) + (y ** 2)) ** 0.5


p = Point(3, 4)
print x
print y

print p.distance_from_origin()