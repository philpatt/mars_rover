
directions = ("N", "E", "S", "W")

class Rover(object):
    print('heres a new rover')
    def __init__(self, x, y, direction, mars):
        self.Mars = mars
        self.direction = direction
        self.x = x
        self.y = y
        self.initial = (self._x, self._y, self._direction)

