#Every rover will have access to the compass. The rover will use this compass to turn left, or turn right based of what direction it is already facing.
compass = ("N", "E", "S", "W")

class Rover(object):
    #Each Rover that is created will have access to all of these functions and the created Landing Area
    # The Rover will always have an initial position that consists of it starting (x,y,direction).
    # While the (x,y,direction) may change, the Landing Area and initial position will remain constant.

    def __init__(self, x, y, direction, landingArea):
        self.x = x
        if (self.x < 0 or self.x > landingArea.x): # Since each rover has access to the Landing Area, we can start by making sure the Rovers initial x and y position is in the landing area.
            raise ValueError('Rover out of landing area, try again!')
            return
        self.y = y
        if (self.y < 0 or self.y > landingArea.y): #
            raise ValueError('Rover out of landing area, try again!')
            return
        self.direction = direction
        self.landingArea = landingArea
        self.initial = (self.x, self.y, self.direction)

    def get_current_position(self):
        # This function allow the rover to access its current position at any point after it is instantiated.
        return (self.x, self.y,)

    def rover_to_intial_position(self):
        # When this function is called the rover will be returned to its intial position
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]

    def xPositionCheck(self, landingArea):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the x value to make sure it is within the landing area dimensions.
        # If is not a valid value, then the rover is returned to its initial position and a Value Error is sent.
        if (self.x < 0 or self.x > landingArea.x):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def yPositionCheck(self, landingArea):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the y value to make sure it is within the landing area dimensions.
        # If is not a valid value, then the rover is returned to its initial position and a Value Error is sent.

        if (self.y < 0 or self.y > landingArea.y):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def directionPositionCheck(self, landingArea):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the directional value to make sure it is a direciton that the Compass .
        # If is not a valid value, then the rover is returned to its initial position and a Value Error is sent.

        if self.direction.upper() not in compass:
            self.rover_to_intial_position()
            raise ValueError('Error: Incorrect direction value, going back to initial position.\n Try again!')
        else:
            return True

    def turnRight(self):
        # Turn Right logic for the Rover
        # if the Rovers direction matches the compasses direction at position 3 ('W' - West), then change the Rover's direction to "N"-North(compass[0]).
        # if the Rover's direction is not 'W'-West, then change the Rover's Direction to the compass direction that is associated with the Rover's direction and increase by 1.
        if compass.index(self.direction) == 3:
            self.direction = compass[0]

        else:
            self.direction = compass[compass.index(self.direction) + 1]


    def turnLeft(self):
        # Turn Left logic for the Rover (opposite of right turn logic)
        # if the Rovers direction matches the compasses direction at position 0 ('N' - North), then change the Rover's direction to "W"-West(compass[3]).
        # if the Rover's direction is not 'N'-North, then change the Rover's Direction to the compass direction that is associated with the Rover's direction and decrease by 1.

        if compass.index(self.direction) == 0:
            self.direction = compass[3]
        else:
            self.direction = compass[compass.index(self.direction) - 1]
    def moveForward(self, landingArea):
        # Move Forward

        if self.direction == "N":
            self.y = self.y + 1
        elif self.direction == "S":
            self.y = self.y - 1
        elif self.direction == "E":
            self.x = self.x + 1

        elif self.direction == "W":
            self.x = self.x - 1
        else:
            self.rover_to_intial_position()
            raise ValueError('ERROR: Incorrect directional value, Rover sent back to initial position')
        for area in self.landingArea.taken:
            if self.get_current_position() == (area[0], area[1]):
                self.rover_to_intial_position()
                raise ValueError('ERROR: Position taken, Rover sent back to intial position!\n Try again!')
