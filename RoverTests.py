import unittest
from Rover import *
from Mars import CreateMarsLandingArea

class RoverTests(unittest.TestCase):
    def testCreateRoverInitialPosition(self):
        landingArea = CreateMarsLandingArea(5, 5)
        rover = CreateRover(1, 2, "N", landingArea)
        x = rover.x
        y = rover.y
        direction = rover.direction
        RoverInitialPosition = x, y, direction
        ExpectedRoverInitialPosition = 1, 2, "N"
        
        self.assertEqual(RoverInitialPosition, ExpectedRoverInitialPosition)


if __name__ == '__main__':
    unittest.main()