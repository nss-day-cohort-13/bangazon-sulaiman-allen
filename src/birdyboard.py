
class Birdyboard():

    def __init__(self, user_object, message_object):

        self.userObject = user_object
        self.messageObject = message_object

    def display_menu(self):
        '''
            Main menu
        '''

        print("\n\n\n\n")
        if(self.userObject.user is not None):
            print("Logged in as {0}".format(self.messageObject.user))
            print()
        else:
            print("Please sign in")
            print("")
        print("#########################################")
        print("##           Birdyboard~~~~~           ##")
        print("#########################################")
        print("1. New User Account\n2. Select User\n3. View Chirps")
        print("4. Public Chirp\n5. Private Chirp\n6. Exit")
        print("\n")

        try:
            choice = int(input("> "))
            return self.menu_selection(choice)
        except ValueError:
            self.display_menu()

    def menu_selection(self, choice):
        '''
            This method performs logic for the display menu method. Takes choice (a string)
            as input.
        '''

        # If the user enters invalid choice, make sure that the error is caught
        # and send them back to the display_menu
        try:
            if (isinstance(choice, int) and (choice > 0 and choice <= 6)):

                if (choice == 1):  # New user account

                    self.userObject.prompt_create_user()

                elif (choice == 2):  # Select user
                    user = self.userObject.select_user()
                    self.messageObject.set_user_for_message_object(user)

                elif (choice == 3):  # View Chirps
                    self.messageObject.view_chirps()

                elif (choice == 4):  # Public Chirp
                    self.messageObject.new_public_chirp()

                elif (choice == 5):  # Private Chirp
                    self.messageObject.load_user_list(self.userObject.users)
                    self.messageObject.new_private_chirp_menu()

                elif (choice == 6):  # Exit
                    print("")
                    print("Goodbye")
                    exit()
            else:
                raise ValueError
        except ValueError:
            self.display_menu()

    def menu_selection_input_test(self, choice):
        '''
            Used for testing logic of menu_selection method.
        '''

        if (isinstance(int(choice), int) and (choice > 0 and choice <= 6)):
            return True


if __name__ == '__main__':
    Birdyboard().display_menu()
