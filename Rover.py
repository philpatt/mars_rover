
directions = ("N", "E", "S", "W")

class Rover(object):
    def __init__(self, x, y, direction, landingArea):
        self.x = x
        self.y = y
        self.direction = direction        
        self.landingArea = landing_area
        self.initial = (self.x, self.y, self.direction)

    def get_current_position(self){
        return (self.x, self.y)
    }
    def rover_to_intial_position(self){
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]   
    }

    def moveForward(self):
        #rover move forwards
        if self.direction == "N":
            self.y = self.y + 1
        elif self.direction == "S":
            self.y = self.y -1
        elif self.direction =='E':
            self.x = self.x + 1
        else:
            self.x = self.x - 1

    def turnRight(self):
        # rover turn right:
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
        if self.direction == "N":
            self.y = self.y + 1
        elif self.direction == "S":
            self.y = self.y -1
        elif self.direction =='E':
            self.x = self.x + 1
        else:
            self.x = self.x - 1
        for area in self.Mars:
            if self.get_current_position() == (area[0], area[1]):
                print('Error: Position taken, rover sent back to intial position! Try again!')
            self.rover_to_intial_position()

    


