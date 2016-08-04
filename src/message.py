import pickle


class Message():

    def __init__(self):
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
        self.users = dict()
        # self.users = load_user_list()

    def set_user_for_message_object(self, user):
        '''
            Sets the currently logged in user for the message object. Takes a string for user
        '''
        self.user = user
        return user

    def load_user_list(self, user_dict):
        self.users = user_dict

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

            for (sender, entry) in self.private_messages.items():
                for recipient in entry:
                    for message_data in self.private_messages[sender][recipient]:
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

        if (choice == 0):
            return
        elif (choice in public_index_dict):
            self.reply_to_public_post(choice)

        elif(choice in private_index_list):
            self.new_private_chirp_menu()

        else:
            print("Please select an option from the list")
            self.view_chirps()

    def reply_to_public_post(self, index):
        '''
            Used for starting/adding to a message thread. These messages dont
            get a unique id and are appended to a list containing the main post
        '''

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
            self.post_reply_to_public_chirp(index, chirp)
        elif(choice == 2):
            self.view_chirps()
        else:
            print()
            print("Please enter a valid choice.")
            print()
            self.reply_to_public_post(index)

    def post_reply_to_public_chirp(self, index, chirp):
        '''
            Posts the reply to a public post to the dictionary. Takes index (int)
            and chirp (string) as arguments.
        '''
        self.public_messages[index].append((self.user, chirp))
        with open('./data/public_messages', 'wb+') as f:
            pickle.dump(self.public_messages, f)
        # self.reply_to_public_post(index)
        return

    def new_public_chirp(self):
        '''
            Creates a new public chirp. Public chirps are stored as a dictionary
            with the key being the message ID. Replies to a public chirp are appended
            to a list as the value of the dictionary so they always appear in the
            correct order.
        '''
        if (not self.user):
            return

        chirp = input("Enter chirp text\n> ")
        self.new_public_chirp_post(chirp)

    def new_public_chirp_post(self, chirp, **kwargs):
        '''
            Method for posting a chirp to the dictionary. Accepts a string as input for chirp
            and optionally 'message_index' (int) and user (string) as kwargs.
        '''
        if(bool(kwargs)):
            message_index = kwargs['message_index']
            user = kwargs['user']

        else:
            message_index = self.message_index
            user = self.user

        messages = [(message_index, user, chirp)]
        self.public_messages[self.message_index] = messages
        self.serialize_messages()
        return

    def new_private_chirp_menu(self):
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
            return

        print("Chirp at:")
        print()
        tempTupList = []

        for key in enumerate(self.users):
            tempTupList.append(key[1])
            print("{0}. {1}".format(key[0] + 1, key[1]))

        print("\n\n")
        print("0. Main Menu")

        selection = input("> ")
        if (selection.isdigit() is False):
            self.new_private_chirp_menu()

        if (int(selection) == 0):
            return

        selection = int(selection) - 1

        recipient = tempTupList[selection]

        chirp = input("Enter chirp text\n> ")

        self.post_private_chirp(chirp, recipient, self.user, self.message_index)

    def post_private_chirp(self, chirp, recipient, user, message_index):
        '''
            Posts the private chirp to dictionary. Takes as input: chirp (string), recipient (string),
            user (string), and message_index(int)
        '''

        try:
            # If the send user already exists as a key in the root dictionary
            if (user in self.private_messages):

                if(recipient in self.private_messages):
                    messages = (self.message_index, user, recipient, chirp)
                    self.private_messages[user][recipient].append(messages)
                else:
                    messages = (self.message_index, user, recipient, chirp)
                    self.private_messages[user][recipient].append(messages)

            # If the user doesnt exit, create it.
            else:
                tempDict = dict()
                messages = [(self.message_index, user, recipient, chirp)]
                tempDict[recipient] = messages
                self.private_messages[user] = tempDict

            self.serialize_messages()
            return

        # except IndexError:
        except:
            print()
            print("Please enter a valid choice.")
            print()
            self.new_private_chirp()

    def deserialize_message_index(self):
        '''
            Load message index from disk
        '''
        with open('./data/message_index', 'rb') as f:
            deserialized = pickle.load(f)
        return deserialized

    def deserialize_public_messages(self):
        '''
            Load public messages from disk
        '''

        with open('./data/public_messages', 'rb+') as f:
            deserialized = pickle.load(f)
            # print(deserialized)
        return deserialized

    def deserialize_private_messages(self):
        '''
            Load private messages from disk
        '''
        with open('./data/private_messages', 'rb+') as f:
            deserialized = pickle.load(f)
        return deserialized

    def serialize_messages(self):
        '''
            Save all other messages to disk
        '''

        self.message_index += 1

        with open('./data/message_index', 'wb+') as f:
            pickle.dump(self.message_index, f)

        with open('./data/public_messages', 'wb+') as f:
            pickle.dump(self.public_messages, f)

        with open('./data/private_messages', 'wb+') as f:
            pickle.dump(self.private_messages, f)
