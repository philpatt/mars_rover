from Mars import CreateMarsLandingArea
from Rover import CreateRover, compass, navigationCommands
import sys

def main():
    # Begin Program here
    print('================================== ')
    print('~~ MARS ROVER TECH CHALLENGE ~~')
    print('\n==================================')

    landingArea = getLandingAreaInput() # Create Landing Area for Rovers to land on

    acquiringAndLandingRovers = True

    while acquiringAndLandingRovers:

        rover = getIntialRoverPositionInput(landingArea) # Acquire a Rover for landing
        landRover(rover, landingArea) # Land Rover on Landing Area based on given command sequence

def getLandingAreaInput():

    landingAreaDimensionsPrompt = '\n--------------\n** Please enter two numbers, separated by a space, to determine the dimensions for the Mars landing Area:\n--------------\n => '

    isCreateLandingAreaRunning = True

    while (isCreateLandingAreaRunning):
        landingAreaInput = input(landingAreaDimensionsPrompt).split(' ')

        if isLandingAreaInputValid(landingAreaInput):

            landingAreaXCoordinate = int(landingAreaInput[0])
            landingAreaYCoordinate = int(landingAreaInput[1])

            landingArea = CreateMarsLandingArea(landingAreaXCoordinate,landingAreaYCoordinate)

            isCreateLandingAreaLoopRunning = False

            return landingArea


def isLandingAreaInputValid(landingAreaInput):
    if len(landingAreaInput) == 2 and landingAreaInput[0].isdigit() and landingAreaInput[1].isdigit():
        return True
    else:
        print('ERROR: Wrong Values. Try Again!')
        return False


def getIntialRoverPositionInput(landingArea):
    # Here is where we create a Rover Object attached to the Landing Area Object
    # We also check too see if the input is 'report' or 'exit', if so, => See user_input_check()
    # Again, a loop is run to ensure that acquiring user input does not terminate the program until all rovers are created and landed.

    while True:
        roverPositionPrompt = "\n--------------\n** Enter a Rover's starting position and direction, separated by spaces.\n* Or enter 'report' to get Rover Report.\n* Or enter: 'end' to terminate:\n--------------\n=> "

        roverInput = userInputCheck(input(roverPositionPrompt),landingArea).split(' ')
        try:
            if 'report' not in roverInput and isInitialRoverPositionInputValid(roverInput):
                rover = CreateRover(int(roverInput[0]), int(roverInput[1]), roverInput[2].upper(),landingArea)
                return rover
        except Exception as err:
            print(err)
            continue


def isInitialRoverPositionInputValid(roverInput):
    if len(roverInput) == 3 and roverInput[0].isdigit(
    ) and roverInput[1].isdigit() and roverInput[2].upper() in compass:
        return True
    else:
        print('ERROR: Wrong Values. Try Again!')
        return False


def userInputCheck(userInput, landingArea):
    if 'end'.upper() in userInput.upper():
        print('========================')
        print('### End Program ###')
        print('\n========================')
        sys.exit()
    elif 'report' in userInput.lower():
        showRoverReport(landingArea)
    return userInput


def landRover(rover,landingArea):
    # Using only a sequence of L, M ,R. The user gives commands for the Rover to take in and see if it can land or not.

    moved = False
    commandSequencePrompt = "\n--------------\nPlease enter a sequence of commands:\nOnly use 'L','R','M' or 'end' to terminate\n--------------\n=> "
    try:
        commands = userInputCheck(input(commandSequencePrompt), landingArea).upper()

        if 'REPORT' not in commands and isCommandSequenceValid(commands):
            navigate(commands, rover, landingArea)
            # If commands are determined valid and the rover object is updated, another check comes to determine
            if (rover.yPositionCheck(landingArea) and rover.xPositionCheck(landingArea) and rover.directionPositionCheck(landingArea)):# Here is where the rover checks if the landing coordinates are acceptable
                landingArea.taken.append([rover.x, rover.y, rover.direction])
                moved = True
    except Exception as err:
        print(err)
    if moved:
        print('\n------------------------------------')
        print('~~~~~~ Rover Landing Success! ~~~~~~')
        print('------------------------------------')

        showRoverReport(landingArea)
        return

def isCommandSequenceValid(commands):
    for command in commands:
        if command not in navigationCommands:
            print('\n----------------------------------------')            
            print("Command Sequence Value Error:")
            print(command,": not available in Navigation Commands.")
            print("Rover Crashed! Attempt New Rover!")
            print('----------------------------------------') 
            return False
    return True

def navigate(commands, rover, landingArea):
    # This is the knowledge the Rover uses to read its commands.
    # If the rover does not read an 'L', 'R', or 'M' then it sends an Error message, returns to its initial position and requests a new set of commands.
    # Otherwise, it uses its own methods to turn 90 degrees, left or right, and move accordingly.
    # After a 'Move Forward' request is made, the rover checks to see if the that space is occupied.
    # If space is occupied, then an Error message, rover is returned to initial position, along with a request for a new set of commands.
    # If space is NOT occupied, then the rover Object is updated and moves on in the land_rover() process.
    try:
        for command in commands:
            if command == navigationCommands[0]:
                rover.turnLeft()  # => see Rover.py for more details
            elif command == navigationCommands[1]:
                rover.turnRight()  # => see Rover.py for more details
            elif command == navigationCommands[2]:
                rover.moveForward(
                    landingArea)  # => see Rover.py for more details
            else:
                raise ValueError('Incorrect directional value')
    except Exception as err:
        raise err

def showRoverReport(landingArea):
    # The Rover Report prints the taken Landing Area list, it also is shown after each succesful landing
    print('\n-----------------------')
    print('*~* Rover Report *~*')
    print('-----------------------')
    print('Landing Area: ' + str(landingArea.x) + ' x ' + str(landingArea.y))
    for rover in landingArea.taken:
        print ("Rover landed at {} {} {}".format(rover[0],rover[1],rover[2]))
    print('-----------------------')

if __name__ == "__main__":
    main()