compass = ["N", "E", "S", "W"]
navigation_commands = ["L","R","M"]

class create_rover(object):
    #Each Rover that is created will have access to all of these functions, the compass, and Navigation Commands and the created Landing Area

    def __init__(self, x, y, direction, landing_area):
        self.x = x
        self.y = y
        self.direction = direction
        self.initial = (self.x, self.y, self.direction)

    def get_current_position(self):
        # This function allow the rover to access its current position at any point after it is instantiated.
        return [self.x, self.y]

    def rover_to_intial_position(self):
        # When this function is called the rover will be returned to its intial position
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]

    def x_position_check(self, landing_area):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the x value to make sure it is within the landing area dimensions.
        if (self.x < 0 or self.x > landing_area.x):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def y_position_check(self, landing_area):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the y value to make sure it is within the landing area dimensions.

        if (self.y < 0 or self.y > landing_area.y):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def direction_position_check(self):
        # This function is used during navigation. After the Rover uses navigate to turn left, turn right, and move forward, this checks the directional value to make sure it is a direciton that the Compass .

        if self.direction.upper() not in compass:
            self.rover_to_intial_position()
            raise ValueError('Error: Incorrect direction value, going back to initial position.\n Try again!')
        else:
            return True

    def turn_right(self):
        # If the Rover's direction matches the compass' direction at position 3 ('W' - West), then change the Rover's direction to "N"-North(compass[0]).
        # If the Rover's direction is not 'W'-West, then change the Rover's Direction to the compass direction that is associated with the Rover's direction and increase by 1.

        if compass.index(self.direction) >= 3:
            self.direction = compass[0]
        else:
            self.direction = compass[compass.index(self.direction) + 1]


    def turn_left(self):
        # if the Rovers direction matches the compasses direction at position 0 ('N' - North), then change the Rover's direction to "W"-West(compass[3]).
        # if the Rover's direction is not 'N'-North, then change the Rover's Direction to the compass direction that is associated with the Rover's direction and decrease by 1.

        if compass.index(self.direction) <= 0:
            self.direction = compass[3]
        else:
            self.direction = compass[compass.index(self.direction) - 1]

    def move_forward(self, landing_area):
        # Move Forward and check to see if that is space is available.
        new_position = self.get_current_position()

        if self.direction == "N":
            new_position[1] += 1
        elif self.direction == "S":
            new_position[1] -= 1
        elif self.direction == "E":
            new_position[0] += 1
        elif self.direction == "W":
            new_position[0] -= 1
        else:
            raise ValueError('ERROR: Incorrect directional value, Rover sent back to initial position')

        # Check if out of bounds or occupied by other rovers
        if self.check_move(new_position[0], new_position[1], landing_area):
            self.x = new_position[0]
            self.y = new_position[1]
        else:
            self.rover_to_intial_position()
            raise ValueError

    def check_move(self, position_x, position_y, landing_area):
        if position_x < 0 or position_y < 0 or position_x >= landing_area.x or position_y >= landing_area.y:
            print('\n---------------------------')
            print('Almost drove out of bounds!\n Rover return to intial position!')
            print('----------------------------')
            return False
        for area in landing_area.taken:
            if (position_x, position_y) == (area[0], area[1]):
                print('\n---------------------------')
                print('Crashed into rover at,',area,'!\nRover return to intial position!')
                print('----------------------------')
                return False
        return True
