# Title: Dictionary Sorting Practice
# Author:
# Date: 12/22/2020
# Purpose: To create a case-insensitive word freqeuncy map
# Testing branch feature

from collections import defaultdict


#
# User Class
#
class User:
    def __init__(self, name):
        self.name = name
        self.ID = None
        self.wordFreq = defaultdict(int)
        self.sortedKeys = None


#############
# Functions #
#############


#
# Generate Word Frequency
#
# Take each word in the input and count up it's occurances
#
def wordFreqKeys(userInput):
    # defaultdict(int): If a key doesn't exist, add it with a default value of 0
    wordFreq = defaultdict(int)
    for word in userInput.casefold().split():
        wordFreq[word] += 1

    # sorted() returns a *list* of key from most freq keys to least freq keys
    sorted_wordFreqKeys = sorted(wordFreq, key=wordFreq.get, reverse=True)

    return wordFreq, sorted_wordFreqKeys


#
# Print Word Frequency
#
def printWordFreq(wordFreq, sortedKeys):
    print("\n   [Word Count]")
    for currentKey in sortedKeys:
        print("   {}: {}".format(currentKey, wordFreq[currentKey]))

    return


def main():
    # Collection of Users
    Users = dict()

    # Instantiate Users and add them to "Users" dictionary
    print("[Message Word Frequency]")

    ID = 0
    userName = input("Input User Name: ")
    while (userName != "-1"):
        # Create a new user
        newUser = User(userName)

        # Get the message
        message = input("{}\'s message: ".format(userName))

        # Generate the word frequency of the message
        wordFreq = wordFreqKeys(message)

        # Assign the word frequency to the new user
        newUser.ID = ID
        newUser.wordFreq = wordFreq[0]
        newUser.sortedKeys = wordFreq[1]

        # Add the new user instance to the dict
        Users.update({userName: newUser})

        # Increment ID by 1 and get next user
        ID += 1
        userName = input("\nNext Name: ")

    # Look Up Names
    print("\n[Name Look Up]")
    userName = input("Look Up Name:  ")
    while (userName != "-1"):
        query = Users.get(userName, None)

        if query != None:
            print("   [User Information]")
            print("   ID: {} Name: {}".format(query.ID, query.name))
            printWordFreq(query.wordFreq, newUser.sortedKeys)

        else:
            print("   {} was not found.".format(userName))

        userName = input("\nLook Up Next Name:  ")


# Run the program (Made to test branching)
main()

print("\nExiting Program. . .")
