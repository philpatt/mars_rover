
directions = ("N", "E", "S", "W")

class Rover(object):
    def __init__(self, x, y, direction, landingArea):
        self.x = x
        self.y = y
        self.direction = direction        
        self.landingArea = landing_area
        self.initial = (self.x, self.y, self.direction)


    def turnRight(self):
        # rover turn right
        
        if directions.index(self.direction) == 3:
            return self.direction = directions[0]
        else:
            return self.directions = directions[directions.index(self.direction) + 1]

    def turnLeft(self):
        # rover turn left
                if directions.index(self.direction) == 0:
            return self.direction = directions[3]
        else:
            return self.directions = directions[directions.index(self.direction) - 1]

    def moveForward(self):
        #rover move forwards

    


