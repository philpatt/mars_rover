¬¬# no rover created on bad input
# bad input 1: cannot land on another rover
# bad input 2: cannot land out of bounds
# exit if landing pad full
# don't move if bad move detected
# check landing area not less than or equal 0

from Mars import create_mars_landing_area
from Rover import create_rover, compass, navigation_commands
import sys

def main():
    print('===============================')
    print('~~ MARS ROVER TECH CHALLENGE ~~')
    print('===============================')

    # 1 - Create Landing Area for Rovers to land on
    landing_area = get_landing_area()

    #2 - Acquire Rovers to land
    acquiring_rovers = True
    while acquiring_rovers:
        # Instantiate Rover
        rover = get_intial_rover_position_input(landing_area)
        # Attempt to land Rover on Landing Area
        land_rover(rover, landing_area)

def get_landing_area():
    landing_area_dimensions_prompt = '\n--------------\n** Please enter two numbers, separated by a space, to determine the dimensions for the Mars landing Area:\n--------------\n => '
    is_create_landing_area_running = True
    while (is_create_landing_area_running):
        landing_area_input = input(landing_area_dimensions_prompt).split(' ')
        if is_landing_area_input_valid(landing_area_input):
            landing_area = create_mars_landing_area(landing_area_input)
            is_create_landing_area_loop_running = False
            return landing_area


def is_landing_area_input_valid(user_input):
    if len(user_input) == 2 and user_input[0].isdigit() and user_input[1].isdigit():
        x = int(user_input[0])
        y = int(user_input[0])
    elif len(user_input) > 2 :
        print('\n----------------------------------')
        print('Error: Too many values. Try Again!')
        print('----------------------------------')
        return False
    else:
        print('\n-------------------------------------------------')
        print('Error: Landing Area can only be numbers! Try again')
        print('-------------------------------------------------')
        return False

    if x > 0 and y > 0:
        print('\n--------------------------------')
        print(x, 'x', y, 'Landing Area Created')
        print('-------------------------------')
        return True
    else:
        print('\n--------------------------------------------')
        print('ERROR: Values need to be above 0! Try Again!')
        print('--------------------------------------------')
        return False


def get_intial_rover_position_input(landing_area):
    # Here is where we create a Rover Object attached to the Landing Area Object
    # 1. make sure input is intergers
    # 2. Make sure rover inbounds
    # 3. Make sure rover not in landing are taken array
    # We also check too see if the input is 'report' or 'exit'

    while True:
        rover_position_prompt = "\n--------------\n** Enter a Rover's starting position and direction, separated by spaces.\n* Or enter 'report' to get Rover Report.\n* Or enter: 'end' to terminate:\n--------------\n=> "

        rover_input = user_input_check(input(rover_position_prompt),landing_area).split(' ')

        try:
            if 'report' not in rover_input and is_rover_input_valid(rover_input) and is_rover_inbounds(rover_input, landing_area) and is_rover_position_taken(rover_input, landing_area):
                rover_x = int(rover_input[0])
                rover_y = int(rover_input[1])
                rover_direction = rover_input[2].upper()
                rover = create_rover(rover_x, rover_y, rover_direction,landing_area)
                return rover
        except ValueError:
            print('Error 1')

def is_rover_input_valid(user_input):

    if len(user_input) == 3 and user_input[0].isdigit() and user_input[1].isdigit() and user_input[2].upper() in compass:
        return True
    elif len(user_input) > 3:
        print('\n--------------------------------------------')
        print('ERROR: You input too many values! Try again!')
        print('--------------------------------------------')
        return False
    else:
        print('\n--------------------------------------------')
        print('ERROR: Please enter correct values for rover!')
        print('--------------------------------------------')
        return False
    return True

def is_rover_position_taken(user_input,landing_area):
    rover = int(user_input[0]),int(user_input[1])
    if len(landing_area.taken) > 0:
        for area in landing_area.taken:
            if rover == (area[0], area[1]):
                print('\n--------------------------------------------')
                print('ERROR: Position taken! Try another position')
                print('--------------------------------------------')
                return False
    return True

def is_rover_inbounds(coordinates, boundary):
    x = int(coordinates[0])
    y = int(coordinates[1])
    if ( x < 0 or x > boundary.x):
        print('\n--------------------------------------------')
        print('ERROR: X Coordinate out of range! Try again!')
        print('--------------------------------------------')
        return False
    elif ( y < 0 or y > boundary.y):
        print('\n--------------------------------------------')
        print('ERROR: Y Coordinate out of range! Try again!')
        print('--------------------------------------------')
        return False
    return True

def user_input_check(user_input, landing_area):
    if 'end'.upper() in user_input.upper():
        print('========================')
        print('### End Program ###')
        print('\n========================')
        sys.exit()
    elif 'report' in user_input.lower():
        show_rover_report(landing_area)
    return user_input

def land_rover(rover,landing_area):
    # Using only a sequence of L, M ,R. The user gives commands for the Rover to take in and see if it can land or not.
    # 1. Make sure Command sequence is valid (only LMR)
    # 2. Make sure rover command sequence allows rover to stay inbounds
    # 3. Make sure rover command sequence doesnt move rover into an occupied spot
    # 4. Check too see if the input is 'report' or 'exit'
    # Return Rover back to initial position if above criteria is not met
    moved = False
    command_sequence_prompt = "\n--------------\nPlease enter a sequence of commands:\nOnly use 'L','R','M' or 'end' to terminate\n--------------\n=> "
    while not moved:
        try:
            commands = user_input_check(input(command_sequence_prompt), landing_area).upper()
            if 'REPORT' not in commands and is_command_sequence_valid(commands):
                navigate(commands, rover, landing_area)
            else:
                raise ValueError
            if (rover.y_position_check(landing_area) and rover.x_position_check(landing_area) and rover.direction_position_check()):
                landing_area.taken.append([rover.x, rover.y, rover.direction])
                moved = True
        except ValueError:
            print('Rover back to', rover.initial)
    if moved:
        print('\n-----------------------------')
        print('~~~~~~ Rover Landed ! ~~~~~~')
        print('----------------------------')
        is_landing_area_full(landing_area)
        show_rover_report(landing_area)
        return

def is_command_sequence_valid(commands):
    if len(commands) <= 0:
        print('=======================================')
        print('No command sequence entered. Try Again!')
        print('\n=====================================')
        return False
    for command in commands:
        if command not in navigation_commands:
            print('\n----------------------------------------')
            print("Command Sequence Value Error:")
            print(command,": not available in Navigation Commands.")
            print('----------------------------------------')
            return False
    return True

def navigate(commands, rover, landing_area):
    # After a 'Move Forward' request is made, the rover checks to see if that space is occupied.
    # If space is NOT occupied, then the rover Object is updated and moves on in the landRover() process.
    for command in commands:
        if command == navigation_commands[0]:
            rover.turn_left()
        elif command == navigation_commands[1]:
            rover.turn_right()
        elif command == navigation_commands[2]:
            rover.move_forward(landing_area)
        else:
            return False
    return True

def show_rover_report(landing_area):
    print('\n-----------------------')
    print('*~* Rover Report *~*')
    print('-----------------------')
    print('Landing Area: ' + str(landing_area.x) + ' x ' + str(landing_area.y))
    print ("Landed Rovers:")
    for rover in landing_area.taken:
        print("{} {} {}".format(rover[0],rover[1],rover[2]))
    print('-----------------------')

def is_landing_area_full(landing_area):
    landing_area_size = int(landing_area.x + 1) * int(landing_area.y + 1)
    if len(landing_area.taken) >= landing_area_size:
        show_rover_report(landing_area)
        sys.exit()

if __name__ == "__main__":
    main()