import unittest
from birdyboard import *


class birdTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.bird = Birdyboard()

    def test_birdyboard_class_is_of_type_birdyboard(self):
        self.assertIsInstance(self.bird, Birdyboard)

    def test_birdyboard_menu_selection_only_takes_numbers_1_through_6(self):
        self.assertEqual(True, Birdyboard().menu_selection_input_test(3))

    def test_birdyboard_menu_selection_throws_value_error_if_outside_range(self):
        self.assertRaises(ValueError, Birdyboard().menu_selection_input_test(9))

    def test_for_user_file_that_doesnt_exist_throws_error(self):
        self.assertRaises(FileNotFoundError, User().file_creation_of_empty_users_test())







if __name__ == '__main__':
    unittest.main()
