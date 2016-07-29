import pickle


def main():

    interests = {
        "Sarah": ["MMA", "Fencing", "Writing"],
        "Michael": ["Hockey", "Gardening", "Cosplay"]
    }

    with open('serialized-interests', 'wb') as f:
        pickle.dump(interests, f)

    with open('serialized-interests', 'rb') as f:
        deserialized = pickle.load(f)
        print(deserialized)

if __name__ == '__main__':
    main()ci24185-a
