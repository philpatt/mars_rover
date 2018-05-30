import unittest
from Mars import *

# Goal for these tests is to make sure that if the user input is valid, the Mars Landing Area object is created successfully
class mars_tests(unittest.TestCase):

    def test_create_mars_landing_area_coordinate_input(self):
        landingArea = create_mars_landing_area(5, 5)
        x = landingArea.x
        y = landingArea.y
        landing_area_coordinates = str(x) + " " + str(y)
        expected_landing_area_coordinates = "5 5"
        self.assertEqual(landing_area_coordinates, expected_landing_area_coordinates)

    def testCreateMarsLandingAreaEmpyTakentList(self):
        landing_area = create_mars_landing_area(5, 5)
        intial_taken_list = landing_area.taken
        empty_list = []
        self.assertEqual(intial_taken_list, empty_list)


if __name__ == '__main__':
    unittest.main()