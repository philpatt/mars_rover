from Main import *
import unittest

# The main goal for these tests is to make sure the input validations are working correctly.

class MainTests(unittest.TestCase):

    def testIsLandingAreaInputValid(self):
        landingAreaInputTrue = ['25', '25']
        self.assertTrue(isLandingAreaInputValid(landingAreaInputTrue), True) # Valid Landing Area Input => True

        landingAreaInputFalse1 = ['25', '25', '25']
        self.assertFalse(isLandingAreaInputValid(landingAreaInputFalse1), False) # Length of input is too long => print Error message and return False

        landingAreaInputFalse2 = ['25', 'N']
        self.assertFalse(isLandingAreaInputValid(landingAreaInputFalse2), False) # Input has incorrect values => print Error message and return False

    def testIsRoverInitialPositionInputValid(self):
        roverInputTrue = ["1", "2", "N"]
        self.assertTrue(isInitialRoverPositionInputValid(roverInputTrue),True) # Valid Rover Input => True

        roverInputFalse1 = ["1", "N", "N"]
        self.assertFalse(isInitialRoverPositionInputValid(roverInputFalse1), False) # Input has incorrect values => False, print Error message

        roverInputFalse2 = ["1", "2", "N", "N"]
        self.assertFalse(isInitialRoverPositionInputValid(roverInputFalse2), False) # Input has too many values => False, print Error message 

    def testIsCommandSequenceValid(self):
        commandsTrue = 'lmlmlmlmm' 
        self.assertTrue(isCommandSequenceValid(commandsTrue),True) # Valid, input not case sensitive => True

        commandsFalse1 = 'LMRD' # Command sequence values not within NavigationCommands => False
        self.assertFalse(isCommandSequenceValid(commandsFalse1),False) # Valid, input not case sensitive => True
    


if __name__ == "__main__":
    unittest.main()