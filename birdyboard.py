import sys
# sys.path.append("./src")
from users import *
# sys.path.append("./data")


class Birdyboard():

    def __init__(self):
        self.userObject = User()
        self.users = self.userObject.load_self_dot_user()
        # self.user = userObject.
        pass
        # try:
        #     self.users = self.deserialize_users()
        # except:
        #     print("Loading of users file failed, creating new one")
        #     print()
        #     self.users = dict()
        # self.user = User().select_user()

    def display_menu(self):

        print("\n\n\n\n")
        if(self.user):
            print("Logged in as {0}".format(self.user))
            print()
        else:
            print("Please sign in")
            print()
        print("#########################################")
        print("##           Birdyboard~~~~~           ##")
        print("#########################################")
        print("1. New User Account\n2. Select User\n3. View Chirps")
        print("4. Public Chirp\n5. Private Chirp\n6. Exit")
        print()

        choice = input("> ")

        return self.menu_selection(choice)

    def menu_selection(self, choice):

        # If the user enters invalid choice, make sure that the error is caught
        # and send them back to the display_menu
        try:
            if (isinstance(int(choice), int) and (choice > 0 and choice <= 6)):

                if (choice == 1):  # New user account
                    # self.create_user()
                    User.create_user()

                elif (choice == 2):  # Select user
                    self.select_user()

                elif (choice == 3):  # View Chirps
                    self.view_chirps()

                elif (choice == 4):  # Public Chirp
                    self.new_public_chirp()

                elif (choice == 5):  # Private Chirp
                    self.new_private_chirp()

                elif (choice == 6):  # Exit
                    print()
                    print("Goodbye")
                    exit()
            else:
                raise ValueError
        except ValueError:
            self.display_menu()

    def menu_selection_input_test(self, choice):

        if (isinstance(int(choice), int) and (choice > 0 and choice <= 6)):
            return True


if __name__ == '__main__':
    Birdyboard().display_menu()
