class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter method are better practice than just accessing an
        # attribute directly return self.x
        return self.y
    def getY(self):
        # Getter method for a Coordinate object's y coordinate.
        return self.y


    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self):
        if self.x == self.y:
            return True

    def __repr__(self):
         return eval(repr())==Coordinate()

c = Coordinate(3, 3)
print c.x, c.y
print c.getX()
print c.__eq__()