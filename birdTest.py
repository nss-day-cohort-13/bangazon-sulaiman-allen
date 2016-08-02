import unittest
from main import *
sys.path.append("./src")
from birdyboard import *
from users import *
from message import *


class birdTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.user_instance = User()
        self.message_instance = Message()
        self.bird_instance = Birdyboard(self.user_instance, self.message_instance)

    def test_birdyboard_class_is_of_type_birdyboard(self):
        self.assertIsInstance(self.bird_instance, Birdyboard)

    def test_birdyboard_menu_selection_only_takes_numbers_1_through_6(self):
        self.assertEqual(True, self.bird_instance.menu_selection_input_test(3))

    def test_birdyboard_menu_selection_throws_value_error_if_outside_range(self):
        self.assertRaises(ValueError, self.bird_instance.menu_selection_input_test(9))

    def test_for_user_file_that_doesnt_exist_throws_error(self):
        self.assertRaises(FileNotFoundError, User.deserialize_users())







if __name__ == '__main__':
    unittest.main()
