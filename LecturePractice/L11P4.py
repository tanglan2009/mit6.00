class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attributes directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        # First make sure 'other' is of the same time
        assert type(other)== type(self)
        # Since 'other' is the same type, test if coordinates are equal
        return self.getX() == other.getX() and self.getY() == other.getY()
