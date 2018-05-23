import unittest
from Rover import *
from Mars import create_mars_landing_area

class rover_tests(unittest.TestCase):
    def test_create_rover_initial_position(self):
        landing_area = create_mars_landing_area((5, 5))
        rover = create_rover(1, 2, "N", landing_area)

        x = rover.x
        y = rover.y
        direction = rover.direction
        rover_initial_position = x, y, direction
        expected_rover_initial_position = 1, 2, "N"

        self.assertEqual(rover_initial_position, expected_rover_initial_position)

    def test_check_move(self):
        landing_area = create_mars_landing_area((5, 5))
        rover = create_rover(1, 2, "N", landing_area)
        self.assertEqual(rover.check_move(rover.x, rover.y, landing_area), True)







if __name__ == '__main__':
    unittest.main()