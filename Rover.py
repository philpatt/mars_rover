
directions = ("N", "E", "S", "W")

class Rover(object):
    def __init__(self, x, y, direction, landingArea):
        self.x = x
        self.y = y
        self.direction = direction        
        self.landingArea = landingArea
        self.initial = (self.x, self.y, self.direction)

    def get_current_position(self):
        return (self.x, self.y)

    def rover_to_intial_position(self):
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]

    def turnRight(self):
        # rover turn right:
        if directions.index(self.direction) == 3:
            self.direction = directions[0]
            print("self.direction:",self.direction)
            
        else:
            self.directions = directions[directions.index(self.direction) + 1]
            print("self.direction:",self.direction)
            

    def turnLeft(self):
        # rover turn left
        if directions.index(self.direction) == 0:
            self.direction = directions[3]
            print("self.direction:",self.direction, type(self.direction))
        else:
            self.directions = directions[directions.index(self.direction) - 1]
            print("self.direction:",self.direction, type(self.direction))

            

    def moveForward(self, landingArea):
        #rover move forwards
        if self.direction == "N":
            self.y = self.y + 1
            print("self.y:",self.y)            
        elif self.direction == "S":
            self.y = self.y - 1
            print("self.y:",self.y)                                  
        elif self.direction =='E':
            self.x = self.x + 1
            print("self.x:",self.x)            
        else:
            self.x = self.x - 1
            print("self.x:",self.x)                        
        for area in self.landingArea.taken:
            if self.get_current_position() == (area[0], area[1]):
                print('Error: Position taken, rover sent back to intial position! Try again!')
                self.rover_to_intial_position()


