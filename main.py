from Mars import MarsPlateau
from Rover import Rover

def intial_rover_position(landingArea):
    # create a rover by inputing an initial position
    rover_input = input("Please enter rover's starting position: ").split(' ')
    rover = Rover(rover_input, landingArea)

def land_rover(landingArea):
    # input directions for the rover to land 
    directions_input = input("Please enter directions to land rover:\nOnly use 'L','R','M' ").split(' ')


def main():
    
    # Main functionality of program


    landing_area_input = input('Please enter size of the landing plateau, separated by a space: ').split(' ')
    landing_area = MarsPlateau(int(landing_area_input[0]), int(landing_area_input[1]))

    rover = create_rover(landing_area) # Create rover
    land_rover(rover, landing_area) # Once rover is created => try to land it based on the given directions

if __name__ == "__main__":
    main()