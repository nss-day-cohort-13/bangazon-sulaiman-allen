import unittest
from main import *
sys.path.append("./src")
from birdyboard import *
from users import *
from message import *
import os


class birdTester(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.user_instance = User()
        self.message_instance = Message()
        self.bird_instance = Birdyboard(self.user_instance, self.message_instance)

    def test_birdyboard_class_is_of_type_birdyboard(self):
        self.assertIsInstance(self.bird_instance, Birdyboard)

    def test_user_class_is_of_type_user(self):
        self.assertIsInstance(self.user_instance, User)

    def test_message_class_is_of_type_message(self):
        self.assertIsInstance(self.message_instance, Message)

    def test_birdyboard_menu_selection_only_takes_numbers_1_through_6(self):
        self.assertEqual(True, self.bird_instance.menu_selection_input_test(3))

    def test_birdyboard_menu_selection_throws_value_error_if_outside_range(self):
        self.assertRaises(ValueError, self.bird_instance.menu_selection_input_test(9))

    def test_user_class_deserialize_users_returns_not_none_if_file_is_not_empty(self):
        self.assertIsNotNone(self.user_instance.deserialize_users())
        # os.path.isfile(fpath) and os.path.getsize(fpath) > 0

    def test_user_creation(self):
        username = "Zorlarg"
        self.user_instance.create_user([username, "Test_User"])
        userlist = User.return_users()
        self.assertEqual(userlist[username][0], username)

    def test_public_chirp_creation(self):
        user = self.user_instance.set_user("Zorlarg")
        message_index = self.message_instance.message_index
        chirp = "Hey guys dont mind me, this is just a test message"
        self.message_instance.new_public_chirp_post(chirp, message_index=message_index, user=user)
        messagelist = self.message_instance.deserialize_public_messages()
        self.assertEqual(messagelist[message_index][0][2], chirp)








if __name__ == '__main__':
    unittest.main()
