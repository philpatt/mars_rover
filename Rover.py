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
        return [self.x, self.y]

    def rover_to_intial_position(self):
        self.x = self.initial[0]
        self.y = self.initial[1]
        self.direction = self.initial[2]

    def x_position_check(self, landing_area):
        # is X within landing areay dimensions
        if (self.x < 0 or self.x > landing_area.x):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def y_position_check(self, landing_area):
        # is y within landing areay dimensions
        if (self.y < 0 or self.y > landing_area.y):
            self.rover_to_intial_position()
            raise ValueError('\nRover out of landing area, and lost in space!\n Try another Rover!')
        else:
            return True

    def direction_position_check(self):
        # is direction part of compass list
        if self.direction.upper() not in compass:
            self.rover_to_intial_position()
            raise ValueError('Error: Incorrect direction value, going back to initial position.\n Try again!')
        else:
            return True

    def turn_right(self):
        if compass.index(self.direction) >= 3:
            self.direction = compass[0]
        else:
            self.direction = compass[compass.index(self.direction) + 1]

    def turn_left(self):
        if compass.index(self.direction) <= 0:
            self.direction = compass[3]
        else:
            self.direction = compass[compass.index(self.direction) - 1]

    def move_forward(self, landing_area):
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
        # if out of bounds or crash in to other rover, return to rovers original spot
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
