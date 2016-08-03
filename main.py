import sys
sys.path.append("./src")
from birdyboard import *
from users import *
# import message
from message import *


class Main():
    def main(self):
        self.user_instance = User()
        self.message_instance = Message()
        self.bird_instance = Birdyboard(self.user_instance, self.message_instance)

        while(True):
            self.bird_instance.display_menu()


if __name__ == '__main__':
    Main().main()
    # User.return_users()
