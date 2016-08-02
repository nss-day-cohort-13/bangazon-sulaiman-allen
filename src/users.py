import sys
import birdyboard
# sys.path.append("..")
# from birdyboard import *
# sys.path.append('./data')


class User():

    def __init__(self):
        self.user = None
        self.bird = birdyboard.Birdyboard()
        # try:
        #     self.users = self.deserialize_users()
        # except:
        #     print("Loading of users file failed, creating new one")
        #     print()
        #     self.users = dict()

    def load_self_dot_user(self):

        try:
            return self.deserialize_users()
        except FileNotFoundError:
            # print("Loading of users file failed, creating new one")
            # print()
            return dict()

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
        self.bird.menu()
        # self.menu()

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
            print("{0}. {1}".format((key[0] + 1), key[1]))
        print("\n\n")
        print("Enter '0' to return to main menu")
        print()

        selection = int(input("> "))

        if (selection == 0):
            self.menu()
        else:
            selection -= 1

        try:
            self.user = tempTupList[selection]
        except IndexError:
            print()
            print("Please select a user from the list")
            print()
            self.select_user()
        self.menu()

    def serialize_users(self):
        '''
            Save self.users to disk.
        '''

        with open('users', 'wb') as f:
            pickle.dump(self.users, f)

    def deserialize_users(self):
        '''
            Load users from disk
        '''

        with open('users', 'rb') as f:
            deserialized = pickle.load(f)
        return deserialized

    def file_creation_of_empty_users_test(self):
        # print("!!!!!!!!!!!!!!!!!!!!!!")
        self.users = self.deserialize_users()
