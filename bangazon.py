import pickle


class Bangazon():

    def __init__(self):
        self.user_name = None
        self.screen_name = None
        self.user = None

    def menu(self):

        print("#########################################")
        print("##           Birdyboard~~~~~           ##")
        print("#########################################")
        print("1. New User Account\n2. Select User\n3. View Chirps")
        print("4. Public Chirp\n5. Private Chirp\n6. Exit")
        print()

        choice = int(input("> "))
        print()

        if (choice == 1):  # New user account
            self.create_user()

        elif (choice == 2):  # Select user
            # This menu chooses from a list of established users to login as.

            # Which user is chriping?
            # 1. Tweedleedee
            # 2. BiffBoffin
            # ...

            print("Which user is chriping?")
            # show self.users here
            self.user = input("> ")

        elif (choice == 3):  # View Chirps

            pass
            # Only the two users involved in a private chirp can see it in their Private Chirps section.
            # << Private Chirps >>
            # 1. BiffBoffin: Hey, you up for ping...
            # 2. Lara_keet: Any idea what Jeff wa...
            # 3. BiffBoffin: Hah, you got wrecked...
            # << Public Chirps >>
            # 4. Tweedleedee: Anybody know a good...
            # 5. Fuzzy: Do NOT try the mega ultra...
            # 6. Velton32: You guys have got to s...
            # ...
            # 9. Main Menu
            # >

            # Selecting an individual chirp takes you to that chirp's comment thread.

            # Tweedleedee: Anybody know a good Thai restaraunt in the area?
            # Fuzzy: Smiling Elephant is really good
            # BiffBoffin: The pad krapow is amazing!
            # ...
            # 1. Reply
            # 2. Back
            # >
        elif (choice == 4):  # Public Chirp
            # Public

            # Enter chirp text
            # >

            # Users can chirp publicly or they can start a private chirp with another user.
            pass

        elif (choice == 5):  # Private Chirp
            # Private

            # Chirp at
            # 1. BiffBoffin
            # 2. Lara_keet
            # ...
            # 9. Cancel
            # >

            # Enter chirp text
            # >
            pass

        elif (choice == 6):  # Exit
            print("Goodbye")
            exit()

    def create_user(self):
        # A user ID number
        # Screen name
        # Full name
        self.user_name = input("Enter full name\n>")
        self.screen_name = input("Enter screen name\n>")
        print()
        print("User '{0}' created".format(self.screen_name))
        print()
        # write user to file
        self.menu()


if __name__ == '__main__':
    bang = Bangazon().menu()
