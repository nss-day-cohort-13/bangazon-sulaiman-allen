#! /home/xalerons/anaconda3/bin/python
import pickle
import random
random.seed()


class Bangazon():

    def __init__(self):
        try:
            self.users = self.deserialize_users()
        except:
            print("Loading of users file failed, creating new one")
            print()
            self.users = dict()

        try:
            self.message_index = self.deserialize_message_index()
        except:
            self.message_index = 1

        try:
            self.public_messages = self.deserialize_public_messages()
        except:
            self.public_messages = dict()

        try:
            self.private_messages = self.deserialize_private_messages()
        except:
            print("Loading of private messages file failed, creating new one")
            self.private_messages = dict()

        self.user = None

    def menu(self):

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
        choice = int(input("> "))
        print()

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

        else:
            print("Please enter a valid choice.")
            self.menu()

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
            This menu chooses from a list of established users to login.
        '''
        # check to make sure a user exists
        if(not any(self.users)):
            print("No users found, please create a new user")
            print("\n\n")
            self.create_user()

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
        '''
            This menu shows all available posts, public and private (to the logged in user)
        '''

        local_private_message_list = list()
        public_index_dict = dict()
        private_index_list = list()

        if (self.user):
            # save entries to a list to have them printed by index_number later
            private_index_list = list()
            print("<< Private Chirps >>")
            # First key = sending user's username
            for (first_key, entry) in self.private_messages.items():
                # Second key = recipeint's username
                for second_key in entry:
                    # self.private_messages[first_key][second_key] is a list like this:
                    # [(2, 'Glorbus', 'Zargon', 'Hey Zarg'), (5, 'Glorbus', 'Zargon', 'Im good, whats going on??')]
                    for message_data in self.private_messages[first_key][second_key]:
                        if(self.user == message_data[1] or self.user == message_data[2]):
                            local_private_message_list.append(message_data)
            # the results are sorted so that the index number is always in the right order
            # therefore, the messages will be too
            for entry in sorted(local_private_message_list):
                print("{0}. {1} - {2}".format(entry[0], entry[1], entry[3]))
                private_index_list.append((entry[0]))
            print("\n\n\n")
        else:
            print("Log in to see private messages.")
            print()

        print("<< Public Chirps >>")
        for (key, value) in self.public_messages.items():
            for list_entry in value:
                if(type(list_entry[0]) == int):  # Only entries that have a post # are shown
                    print("{0}. {1} - {2}".format(list_entry[0], list_entry[1], list_entry[2]))
                    public_index_dict[key] = [key, list_entry]
        print()
        print("0. Main Menu")
        print()
        choice = int(input("> "))
        print()

        if (choice in public_index_dict):
            self.reply_to_public_post(choice)

        elif(choice in private_index_list):
            print("choice is private")

    def reply_to_public_post(self, index):
        '''
            Used for starting/adding to a message thread. These messages dont
            get a unique id and are appended to a list containing the main post
        '''

        # Selecting an individual chirp takes you to that chirp's comment thread.
        # Tweedleedee: Anybody know a good Thai restaraunt in the area?
        # Fuzzy: Smiling Elephant is really good
        # BiffBoffin: The pad krapow is amazing!
        # ...
        # 1. Reply
        # 2. Back
        # >

        # print the message before adding to the post
        for post in self.public_messages[index]:
            if(type(post[0]) == int):  # This is the root post
                print("{0}: {1}".format(post[1], post[2]))
            else:
                print("{0}: {1}".format(post[0], post[1]))
        print()
        print("1. Reply")
        print("2. Back")
        choice = int(input("> "))
        if (choice == 1):
            chirp = input("Enter chirp text\n> ")
            self.public_messages[index].append((self.user, chirp))
            with open('public_messages', 'wb+') as f:
                pickle.dump(self.public_messages, f)
            self.reply_to_public_post(index)
        elif(choice == 2):
            self.view_chirps()
        else:
            print("Please enter a valid choice.")
            self.reply_to_public_post(index)

    def new_public_chirp(self):
        '''
            Creates a new public chirp. Public chirps are stored as a dictionary
            with the key being the message ID. Replies to a public chirp are appended
            to a list as the value of the dictionary so they always appear in the
            correct order.
        '''
        if (not self.user):
            # print(chr(27) + "[2J")
            print("Please select a user first")
            print()
            self.menu()

        chirp = input("Enter chirp text\n> ")

        messages = [(self.message_index, self.user, chirp)]
        self.public_messages[self.message_index] = messages

        print("self.public_messages = {0}".format(self.public_messages))

        self.serialize_messages()
        self.menu()

    def new_private_chirp(self):
        '''
            Creates a new private chirp. This dictionary is created seperately because it
            uses a different layout than the public dictionary. Posts fall under the poster's
            username as the dictionary key. The user being chirped at is created as a new
            dictionary key under the poster's key for faster indexing and more logical
            layout. The public and private chirps are also stored as 2 different files.
            The 2 dictionaries/files also improve speed (don't have to read/write all
            posts from one long file)/security as the private chirp file can be given
            different permissions.
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

        # If the user doesnt exit, create it.
        else:
            tempDict = dict()
            messages = [(self.message_index, self.user, recipient, chirp)]
            tempDict[recipient] = messages
            self.private_messages[self.user] = tempDict

        self.serialize_messages()
        print(self.private_messages)
        self.menu()

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
