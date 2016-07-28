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
            self.select_user()

        elif (choice == 3):  # View Chirps
            self.view_chirps()

        elif (choice == 4):  # Public Chirp
            self.new_public_chirp()

        elif (choice == 5):  # Private Chirp
            self.new_private_chirp()

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

    def select_user(self):

        # This menu chooses from a list of established users to login as.
        print("Which user is chriping?")
        # show self.users here
        # 1. Tweedleedee
        # 2. BiffBoffin
        # ...
        self.user = input("> ")

    def view_chirps(self):

        # Only the two users involved in a private chirp can see it in their Private Chirps section.
        print("<< Private Chirps >>")
        # 1. BiffBoffin: Hey, you up for ping...
        # 2. Lara_keet: Any idea what Jeff wa...
        # 3. BiffBoffin: Hah, you got wrecked...

        print("<< Public Chirps >>")
        # 4. Tweedleedee: Anybody know a good...
        # 5. Fuzzy: Do NOT try the mega ultra...
        # 6. Velton32: You guys have got to s...
        print("0. Main Menu")
        print()
        choice = int(input("> "))

        # Selecting an individual chirp takes you to that chirp's comment thread.

        # Tweedleedee: Anybody know a good Thai restaraunt in the area?
        # Fuzzy: Smiling Elephant is really good
        # BiffBoffin: The pad krapow is amazing!
        # ...
        # 1. Reply
        # 2. Back
        # >
        pass

    def new_public_chirp(self):

        chirp = input("Enter chirp text\n> ")

        # Users can chirp publicly or they can start a private chirp with another user.

        # A chirp ID number
        # Who authored the chirp
        # Is this a public or private chirp
        # Who the chirp is to (if applicable)
        # The text content of the chirp

    def new_private_chirp(self):
        # Private

        # Chirp at
        # 1. BiffBoffin
        # 2. Lara_keet
        # ...
        # 9. Cancel
        # >

        chirp = input("Enter chirp text\n> ")


if __name__ == '__main__':
    bang = Bangazon().menu()
