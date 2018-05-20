from Mars import MarsLandingArea
from Rover import Rover, directions




def navigate(instructions,rover, landingArea):
    # use commands to navigate the rover to lan
    # if rover moves out of bounds, sent rover back to intial position and try again
    try:
        print("instructions arrive at navigate")
        for instruction in instructions:
            print("indv instruction: "+ instruction)
            if instruction == "L":
                print("TurnLeft")                
                rover.turnLeft()

            elif instruction == "R":
                print("TurnRight")                                
                rover.turnRight()
            else:
                print("MoveForward")                                
                rover.moveForward(landingArea)
    except Exception as err:
        print("Nav ERROR: " + err)
        commands = input("Error: " + err + ". Try another command sequence! ")
        rover.rover_to_intial_position()
        navigate(commands, rover)

def get_intial_rover_position(landingArea):
    # create a rover by inputing an initial position
    while True:
        rover = None
        rover_input = input("Please enter rover's starting position and direction: ").split()
        print('rover input:',rover_input)
        print("landingArea: x-", landingArea.x,"y-", landingArea.y)
        
        try:
            rover = Rover(int(rover_input[0]), int(rover_input[1]), rover_input[2],landingArea)
        except Error as err:
            print(err)
            continue

        if rover is not None:
            print("rover.initial:", rover.initial)
            return rover

def land_rover(rover,landingArea):
    # input directions for the rover to land 

    while True:
        moved = False
        try:
            commands = input("Please enter a sequence of commands:\nOnly use 'L','R','M' ").upper()
            print('these are the commands:',commands)
            navigate(commands, rover, landingArea)
            print('finish navigate')
            landingArea.taken.append((rover.x, rover.y, rover.direction))
            moved = True
        except Exception as err:
            print('ERROR: ',err)
            continue
        if moved:
            print('moved!')
            return
            
def show_landed_rovers(landingArea):
    print('--------------')
    for rover in landingArea.taken:
        print ("{},{},{}".format(rover[0],rover[1],rover[2]))
    SystemExit


def main():
    
    # Main functionality of program

    end_loop = False
    while (not end_loop):
        landing_area_input = input('Please enter size of the landing plateau, separated by a space: ').split(' ')
        landingArea = MarsLandingArea(int(landing_area_input[0]), int(landing_area_input[1]))
        end_loop = True

    while True:
        rover = get_intial_rover_position(landingArea) # Create rover

        land_rover(rover, landingArea) # Once rover is created => try to land it based on the given directions
        show_landed_rovers(landingArea)


if __name__ == "__main__":
    main()