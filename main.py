from Mars import MarsLandingArea
from Rover import Rover, directions
import sys

def navigate(commands,rover,landingArea):
    # This is the knowledge the Rover uses to read its commands.
    # If the rover does not read an 'L', 'R', or 'M' then it sends an Error message, returns to its initial position and requests a new set of commands.
    # Otherwise, it uses its own methods to turn 90 degrees, left or right, and move accordingly.    
    # After a 'Move Forward' request is made, the rover checks to see if the that space is occupied.
    # If space is occupied, then an Error message, rover is returned to initial position, along with a request for a new set of commands.
    # If space is NOT occupied, then the rover Object is updated and moves on in the land_rover() process.

    try:
        for command in commands:
            if command == "L":
                rover.turnLeft() # => see Rover.py for more details
            elif command == "R":  
                rover.turnRight() # => see Rover.py for more details
            elif command == "M":     
                rover.moveForward(landingArea) # => see Rover.py for more details
            else:
                raise ValueError('Incorrect directional value')
    except Exception as err:
        raise err
    

def get_intial_rover_position(landingArea):
    # Here is where we create a Rover Object attached to the Landing Area Object
    # We also check too see if the input is 'report' or 'exit', if so, => See user_input_check()
    # Again, a loop is run to ensure that acquiring user input does not terminate the program until all rovers are created and landed.
    while True:
        rover = None
        rover_input = user_input_check(input("\n--------------\n** Enter a Rover's starting position and direction.\n* Or enter 'report' to get Rover Report.\n* Or enter: 'end' to terminate:\n--------------\n=> "), landingArea).split()
        try:
            if 'report' not in rover_input:
                rover = Rover(int(rover_input[0]), int(rover_input[1]), rover_input[2].upper(),landingArea)
        except Exception as err:
            print(err)
            continue

        # If input values are valid, a new Rover is create and sent for landing => land_rover()                      
        if rover is not None:
            return rover

def user_input_check(userInput, landingArea):
    # Here is where we check to see if the user has requested to a Rover Report status or wants to exit the program.
    # Regardless , the user input is return to whatever function it was acquired.

    if 'end'.upper() in userInput.upper():
        print('\n========================\n### End Program ###\n========================\n')                
        sys.exit()
    elif 'report' in userInput.lower():
        show_landed_rovers(landingArea)
    return userInput


def land_rover(rover,landingArea):
    # Using only a sequence of L, M ,R. The user gives commands for the Rover to take in and see if it can land or not.
    # If there is a Rover already occupying the attempted landing position, the rover will alert an Error Message and return to its initail position.
    # If the Rover is ordered to try and land outside of the Landing Area, it will alert an Error Message and return to its initial position.

        moved = False
        try:
            commands = user_input_check(input("\n--------------\nPlease enter a sequence of commands:\nOnly use 'L','R','M' or 'end' to terminate\n--------------\n=> "),landingArea).upper()
            if 'REPORT' not in commands:
                # Here is where the commands are sent with the Rover to be calculated and to determine if the spot is taken by another Rover.              
                navigate(commands, rover, landingArea) # => Here is all the knowledge for the Rover to compute the sequence of commands

                # If commands are determined valid and the rover object is updated, another check comes to determine
                if (rover.yPositionCheck(landingArea) and rover.xPositionCheck(landingArea) and rover.directionPositionCheck(landingArea)):# Here is where the rover checks if the landing coordinates are acceptable 
                    landingArea.taken.append([rover.x, rover.y, rover.direction])
                moved = True
        except Exception as err:
            print(err)

        if moved:                
            print('Rover Landing Success!')
            show_landed_rovers(landingArea)
            return
            
def show_landed_rovers(landingArea):
    # Here is where we present the Rover Report
    # The Rover Report prints the taken Landing Area list, it also is shown after each succesful landing
    print('-----------------------\n ** Rover Report ** \n-----------------------\nMars landing area:\n'+ str(landingArea.x) + ' x ' + str(landingArea.y)+'\n')
    
    for rover in landingArea.taken:
        print ("{} {} {}".format(rover[0],rover[1],rover[2]))
    print('-----------------------')



def main():

    # This where the program is initiated.
    # A loop is used to allow the input to not terminate until a Landing Object is created
    print('\n================================\n MARS ROVER TECH CHALLENGE \n================================\n')
    end_loop = False
    while (not end_loop):
        landing_area_input = input('** Please enter two numbers, separated by a space, to determine the dimensions for the Mars landing Area:\n--------------\n => ').split(' ')
        if len(landing_area_input) == 2 and landing_area_input[0].isdigit() and landing_area_input[1].isdigit():
            landingArea = MarsLandingArea(int(landing_area_input[0]), int(landing_area_input[1]))
            end_loop = True
        else:
            print('Please enter valid dimensions for landing plateau')

    # Once Landing Area dimensions are determined, the Landing Area is passed to the where the Rover's intial position is, and assigned the created rover.
    # while True:
        rover = get_intial_rover_position(landingArea) # Create Rover and initial position

    # After initial Rover position is set, acquire sequence of commands to attempt to land Rover. 
    # Also, keep track of the landing area to see if there is already a rover that has landed.
        land_rover(rover, landingArea) # land Rover based on given instructions
    
    


if __name__ == "__main__":
    main()