import pickle
import random
random.seed()


class User():

    def __init__(self):
        try:
            self.users = self.deserialize_users()
        except:
            print("Loading of users file failed, creating new one")
            print("")
            self.users = dict()

        self.user = None

    def prompt_create_user(self):
        '''
            Menu for creating a new user
        '''

        full_name = input("Enter full name\n>")
        screen_name = input("Enter screen name\n>")
        print()
        print("User '{0}' created".format(screen_name))
        print()

        self.create_user(["%05d" % random.randint(0, 99999), screen_name, full_name])

    def create_user(self, user_list_object):
        '''
            Creates new user and pushes user to database
        '''
        # self.users[screen_name] = ["%05d" % random.randint(0, 99999), screen_name, full_name]

        self.users[user_list_object[1]] = user_list_object

        self.serialize_users()
        return

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
            return
        else:
            selection -= 1

        try:
            self.user = tempTupList[selection]
        except IndexError:
            print()
            print("Please select a user from the list")
            print()
            self.select_user()
        return

    def serialize_users(self):
        '''
            Save self.users to disk.
        '''

        with open('data/user_data', 'wb') as f:
            pickle.dump(self.users, f)

    def deserialize_users(self):
        '''
            Load users from disk
        '''

        with open('data/user_data', 'rb') as f:
            deserialized = pickle.load(f)
        return deserialized
