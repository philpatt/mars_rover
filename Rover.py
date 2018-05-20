


directions = ("N", "E", "S", "W")

class Rover(object):
    def __init__(self, x, y, direction, landingArea):
        self.x = x
        if (self.x < 0 or self.x > landingArea.x):
            raise ValueError('Rover out of landing area, try again!')
            return
        self.y = y
        if (self.y < 0 or self.y > landingArea.y):
            raise ValueError('Rover out of landing area, try again!')
            return
        
        self.direction = direction
        self.landingArea = landingArea
        self.initial = (self.x, self.y, self.direction)

    def get_current_position(self):
        return (self.x, self.y,)

    def rover_to_intial_position(self):
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]

    def xPositionCheck(self, landingArea):
        print('###self.x',self.x)
        if (self.x < 0 or self.x > landingArea.x):
            self.rover_to_intial_position()            
            raise ValueError('rover out of landing area, going back to initial position.\n Try again!')
        else:
            print('x coordinate checks out')
            return True            

    def yPositionCheck(self, landingArea):
        if (self.y < 0 or self.y > landingArea.y):
            self.rover_to_intial_position()
            raise ValueError('rover out of landing area, go back to intial position.\n Try again!')
        else:
            print('y coordinate checks out')
            return True

    def directionPositionCheck(self, landingArea):
        if self.direction.upper() not in directions:
            self.rover_to_intial_position()            
            raise ValueError('incorrect direction value, going back to initial position.\n Try again!')
        else:
            print('directional checks out')
            return True
   

    def turnRight(self):
        # rover turn right:
        if directions.index(self.direction) == 3:
            self.direction = directions[0]
            print("self.direction:",self.direction)
            
        else:
            self.direction = directions[directions.index(self.direction) + 1]
            print("self.direction:",self.direction)
            

    def turnLeft(self):
        # rover turn left
        if directions.index(self.direction) == 0:
            self.direction = directions[3]
            print("self.direction:",self.direction)
        else:
            self.direction = directions[directions.index(self.direction) - 1]
            print("self.direction:",self.direction)

    def moveForward(self, landingArea):
        #rover move forwards
        if self.direction == "N":
            self.y = self.y + 1
            print("self.y:",self.y)            
        elif self.direction == "S":
            self.y = self.y - 1
            print("self.y:",self.y)                                  
        elif self.direction == "E":
            self.x = self.x + 1
            print("self.x:",self.x)            
        elif self.direction == "W":
            self.x = self.x - 1
            print("self.x:",self.x) 
        else:
            self.rover_to_intial_position()
            print('Incorrect directional value, Rover sent back to initial position')               
        for area in self.landingArea.taken:
            if self.get_current_position() == (area[0], area[1]):
                self.rover_to_intial_position()                
                raise ValueError('ERROR: Position taken, Rover sent back to intial position! Try again!')



