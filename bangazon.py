import pickle
import random
random.seed()


class Bangazon():

    def __init__(self):
        try:
            self.users = self.deserialize_users()
        except:
            print("Loading of file failed, creating new one")
            print()
            self.users = dict()

        try:
            self.message_index = self.deserialize_message_index()
        except:
            print("Index = 0")
            self.message_index = 0

        try:
            self.public_messages = self.deserialize_public_messages()
        except:
            self.public_messages = dict()

        try:
            self.private_messages = self.deserialize_private_messages()
        except:
            print("Loading of private messages file failed, creating new one")
            self.private_messages = dict()

        self.user_name = None
        self.screen_name = None
        self.user = None

    def menu(self):

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
        choice = int(input("> "))

        # print(chr(27) + "[2J")

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
        '''
            Menu for creating a new user
        '''

        full_name = input("Enter full name\n>")
        screen_name = input("Enter screen name\n>")
        print()
        print("User '{0}' created".format(screen_name))
        print()

        self.users[screen_name] = ["%05d" % random.randint(0, 99999), screen_name, full_name]
        self.serialize_users()
        self.menu()

    def select_user(self):
        '''
            This menu chooses from a list of established users to login as.
        '''

        print("Which user is chriping?")

        # make temporary tuple list to bind the key to value to be used by dictionary
        tempTupList = []

        for key in enumerate(self.users):
            tempTupList.append(key[1])
            print("{0}. {1}".format(key[0], key[1]))

        selection = int(input("> "))
        self.user = tempTupList[selection]
        # print(chr(27) + "[2J")
        self.menu()

    def view_chirps(self):

        # Only the two users involved in a private chirp can see it in their Private
        # Chirps section.
        print("<< Private Chirps >>")
        [print("{0}. {1}: {2}".format(value[0], value[1], value[2])) for (key, value) in self.private_messages.items() if value[1] == self.user or value[2] == self.user]
        print()
        print()
        # 1. BiffBoffin: Hey, you up for ping...
        # 2. Lara_keet: Any idea what Jeff wa...
        # 3. BiffBoffin: Hah, you got wrecked...

        print("<< Public Chirps >>")
        # if self.public_messages not 
        [print("{0}. {1}: {2}".format(value[0], value[1], value[2])) for (key, value) in self.public_messages.items()]

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

        '''
            Creates a new public chirp
        '''
        if (not self.user):
            # print(chr(27) + "[2J")
            print("Please select a user first")
            print()
            self.menu()

        chirp = input("Enter chirp text\n> ")

        if (self.public_messages[self.user]):
            self.public_messages[self.user] += {self.message_index, self.user, chirp}

        else:
            self.public_messages[self.user] = [{self.message_index, self.user, chirp}]
            # self.public_messages[self.user] = (self.message_index, self.user, chirp)

        self.serialize_messages()
        self.menu()

    def new_private_chirp(self):
        '''
            Creates a new private chirp
        '''
        if (not self.user):
            # print(chr(27) + "[2J")
            print("Please select a user first")
            print()
            self.menu()

        print("Chirp at:")
        print()

        tempTupList = []

        for key in enumerate(self.users):
            tempTupList.append(key[1])
            print("{0}. {1}".format(key[0], key[1]))

        selection = int(input("> "))
        recipient = tempTupList[selection]

        chirp = input("Enter chirp text\n> ")

        # If the send user already exists as a key in the root dictionary
        if (self.user in self.private_messages):

            message = (self.message_index, self.user, recipient, chirp)
            self.private_messages[self.user][recipient].append(message)

        # If the user doesnt exit, create it. The user being chirped at is created
        # as a new dictionary key for faster indexing and more logical layout.
        else:
            tempDict = dict()
            messages = [(self.message_index, self.user, recipient, chirp)]
            tempDict[recipient] = messages
            self.private_messages[self.user] = tempDict

        self.serialize_messages()
        print(self.private_messages)
        self.menu()

        # Private

        # Chirp at
        # 1. BiffBoffin
        # 2. Lara_keet
        # ...
        # 9. Cancel
        # >
    def deserialize_users(self):

        with open('users', 'rb') as f:
            deserialized = pickle.load(f)
        return deserialized

    def deserialize_message_index(self):
        with open('message_index', 'rb') as f:
            deserialized = pickle.load(f)
        return deserialized

    def deserialize_public_messages(self):

        with open('public_messages', 'rb+') as f:
            deserialized = pickle.load(f)
        return deserialized

    def deserialize_private_messages(self):
        with open('private_messages', 'rb+') as f:
            deserialized = pickle.load(f)
        return deserialized

    def serialize_users(self):

        with open('users', 'wb') as f:
            pickle.dump(self.users, f)

    def serialize_messages(self):

        self.message_index += 1

        with open('message_index', 'wb+') as f:
            pickle.dump(self.message_index, f)

        with open('public_messages', 'wb+') as f:
            pickle.dump(self.public_messages, f)

        with open('private_messages', 'wb+') as f:
            pickle.dump(self.private_messages, f)


if __name__ == '__main__':
    bang = Bangazon().menu()
