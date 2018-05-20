from Mars import MarsPlateau
from Rover import Rover, directions

def get_intial_rover_position(landingArea):
    # create a rover by inputing an initial position
    rover = None
    while not Rover:
        rover_input = input("Please enter rover's starting position and direction: ").split(' ')
        try:
            rover = Rover(int(rover_input[0]), int(rover_input[1]), rover_input[2], landingArea)
        Exception Error as err:
            print(err)
    return rover

def land_rover(rover,landingArea):
    # input directions for the rover to land 
    commands_input = input("Please enter a sequence of commands:\nOnly use 'L','R','M' ").split()
    navigate(commands_input, landingArea)
    mars.taken.append((rover.x, rover.y, rover.direction))

def navigate(commands,rover):
    # use commands to navigate the rover to land
    # if rover moves out of bounds, sent rover back to intial position and try again
    try:
        for command in commands:
            if command == "L":
                rover.turnLeft()
            elif command = "R":
                rover.turnRight()
            else:
                rover.moveForward()
    except Exception as err:
        commands = input("Try another command sequence! ")
        rover.rover_to_intial_position()
        move(commands, rover)

def main():
    
    # Main functionality of program


    landing_area_input = input('Please enter size of the landing plateau, separated by a space: ').split(' ')
    landing_area = MarsPlateau(int(landing_area_input[0]), int(landing_area_input[1]))

    rover = get_intial_rover_position(landing_area) # Create rover
    land_rover(rover, landing_area) # Once rover is created => try to land it based on the given directions

if __name__ == "__main__":
    main()