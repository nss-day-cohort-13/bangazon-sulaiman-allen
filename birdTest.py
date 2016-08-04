import unittest
from main import *
from birdyboard import *
from users import *
from message import *
import os
sys.path.append("./src")


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

    def test_reply_to_messages(self):
        user = self.message_instance.set_user_for_message_object("Tractor Ryan")
        chirp = "Far out man"
        message_index = self.message_instance.message_index - 1
        self.message_instance.post_reply_to_public_chirp(message_index, chirp)
        public_messages_dict = self.message_instance.public_messages
        self.assertEqual(public_messages_dict[message_index][1][1], chirp)

    def test_private_chirp_creation(self):
        chirp = "Hey this is just a test to see if private chirp creation is working"
        recipient = "Zorlarg"
        user = self.user_instance.set_user("Slermo")
        message_index = self.message_instance.message_index
        self.message_instance.post_private_chirp(chirp, recipient, user, message_index)
        private_messages_dict = self.message_instance.private_messages
        self.assertEqual(private_messages_dict[user][recipient][0][3], chirp)

    def test_set_user_returns_proper_user(self):
        self.user_instance.set_user("Slermo")
        self.assertEqual(self.user_instance.user, "Slermo")

    def test_set_user_for_message_object_method(self):
        self.message_instance.set_user_for_message_object("Zorlarg")
        self.assertEqual(self.message_instance.user, "Zorlarg")


if __name__ == '__main__':
    unittest.main()
