from Main import *
import unittest

class MainTests(unittest.TestCase):

    def testIsLandingAreaInputValid(self):
        landingAreaInputTrue = '25', '25'
        self.assertTrue(isLandingAreaInputValid(landingAreaInputTrue), True)

        landingAreaInputFalse = '25', '25', '25'
        self.assertFalse(isLandingAreaInputValid(landingAreaInputFalse), False)

    

if __name__ == "__main__":
    unittest.main()