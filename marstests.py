import unittest
from Mars import *



class MarsTests(unittest.TestCase):

    def testCreateMarsLandingAreaCoordinateInput(self):
        landingArea = CreateMarsLandingArea(5, 5)
        x = landingArea.x
        y = landingArea.y
        landingAreaCoordinates = str(x) + " " + str(y)
        ExpectedLandingAreaCoordinates = "5 5"
        self.assertEqual(landingAreaCoordinates,ExpectedLandingAreaCoordinates)

    def testCreateMarsLandingAreaEmpyTakentList(self):
        landingArea = CreateMarsLandingArea(5, 5)
        intialTakenList = landingArea.taken
        emptylist = []
        self.assertEqual(intialTakenList, emptylist)


if __name__ == '__main__':
    unittest.main()