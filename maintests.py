from Main import *
import unittest

# The main goal for these tests is to make sure the input validations are working correctly.

class main_tests(unittest.TestCase):

    def test_is_landing_area_input_valid(self):
        landing_area_input_true = ['25', '25']
        self.assertTrue(is_landing_area_input_valid(landing_area_input_true), True) # Valid Landing Area Input => True

        landing_area_input_false1 = ['25', '25', '25']
        self.assertFalse(is_landing_area_input_valid(landing_area_input_false1), False) # Length of input is too long => print Error message and return False

        landing_area_input_false2 = ['25', 'N']
        self.assertFalse(is_landing_area_input_valid(landing_area_input_false2), False) # Input has incorrect values => print Error message and return False

    def test_is_rover_input_valid(self):
        rover_input_true = ["1", "2", "N"]
        self.assertTrue(is_rover_input_valid(rover_input_true),True)  # Valid Rover Input => True

        rover_input_false1 = ["1", "N", "N"]
        self.assertFalse(is_rover_input_valid(rover_input_false1),False)  # Input has incorrect values => False, print Error message

        rover_input_false2 = ["1", "2", "N", "N"]
        self.assertFalse(is_rover_input_valid(rover_input_false2), False) # Input has too many values => False, print Error message

    def test_is_command_sequence_valid(self):
        commands_true = 'lmlmlmlmm'.upper()
        self.assertTrue(is_command_sequence_valid(commands_true),True) # Valid, input not case sensitive => True

        commands_false1 = 'LMRD' # Command sequence values not within NavigationCommands => False
        self.assertFalse(is_command_sequence_valid(commands_false1),False) # Valid, input not case sensitive => True



if __name__ == "__main__":
    unittest.main()