from Mars import MarsLandingArea
from Rover import Rover, directions
import sys

def navigate(instructions,rover,landingArea):
    # use commands to navigate the rover to lan
    # if rover moves out of bounds, sent rover back to intial position and try again
    try:
        for instruction in instructions:
            if instruction == "L":
                rover.turnLeft()
            elif instruction == "R":  
                rover.turnRight()
            elif instruction == "M":     
                rover.moveForward(landingArea)
            else:
                raise ValueError('Incorrect directional value')
    except Exception as err:
        raise err



def get_intial_rover_position(landingArea):
    # create a rover by inputing an initial position
    while True:
        rover = None
        rover_input = user_input_check(input("\n--------------\n** Enter a Rover's starting position and direction.\n* Or enter 'report' to get Rover Report.\n* Or enter: 'end' to terminate:\n--------------\n=> "), landingArea).split()

        try:
            if 'report' not in rover_input:
                rover = Rover(int(rover_input[0]), int(rover_input[1]), rover_input[2],landingArea)
        except Exception as err:
            print(err)
            continue

        if rover is not None:
            return rover

def user_input_check(userInput, landingArea):
    if 'end'.upper() in userInput.upper():
        print('\n========================\n### End Program ###\n========================\n')                
        sys.exit()
    elif 'report' in userInput.lower():
        show_landed_rovers(landingArea)
    return userInput


def land_rover(rover,landingArea):
    # input directions for the rover to land 
    while True:
        moved = False
        try:
            commands = user_input_check(input("\n--------------\nPlease enter a sequence of commands:\nOnly use 'L','R','M' or 'end' to terminate\n--------------\n=> "),landingArea).upper()
            if 'REPORT' not in commands:
                navigate(commands, rover, landingArea)
                
                if (rover.yPositionCheck(landingArea) and rover.xPositionCheck(landingArea) and rover.directionPositionCheck(landingArea)):
                    landingArea.taken.append([rover.x, rover.y, rover.direction])
                moved = True
        except Exception as err:
            print(err)
            # continue
        if moved:
            # for i in range(0,len(landingArea.taken)):
            #     if rover.get_current_position() == (landingArea.taken[i][0],landingArea.taken[i][0]):
            #         moved = False
                
            print('Rover Landing Success!')
            show_landed_rovers(landingArea)
            return
            
def show_landed_rovers(landingArea):
    print('-----------------------\n ** Rover Report ** \n-----------------------\nMars landing area:\n'+ str(landingArea.x) + ' x ' + str(landingArea.y)+'\n')
    
    for rover in landingArea.taken:
        print ("{} {} {}".format(rover[0],rover[1],rover[2]))
    print('-----------------------')

        
    


def main():
    
    # Main functionality of program
    print('\n================================\n START MARS ROVER CHALLENGE \n================================\n')
    end_loop = False
    while (not end_loop):
        landing_area_input = input('** Please enter two numbers, separated by a space, to determine the dimensions for the Mars landing Area:\n--------------\n => ').split(' ')
        if len(landing_area_input) == 2 and landing_area_input[0].isdigit() and landing_area_input[1].isdigit():
            landingArea = MarsLandingArea(int(landing_area_input[0]), int(landing_area_input[1]))
            end_loop = True
        else:
            print('Please enter valid size of landing plateau')

    while True:
        rover = get_intial_rover_position(landingArea) # Create rover
        land_rover(rover, landingArea) # land Rover based on given instructions
    
    # print("\n=============================")
    # show_landed_rovers(landingArea)
    # print("\n=============================")
    


if __name__ == "__main__":
    main()