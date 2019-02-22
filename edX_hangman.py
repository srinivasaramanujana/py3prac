# Hangman game

import random
import string

WORDLIST_FILENAME = 'C:\\Users\\ABC\\Desktop\\Docs\\Hangman\\words.txt'

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word l ist, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    accum = ''

    for i in secretWord:
        if i in lettersGuessed:
            accum = accum + i
            if len(secretWord) == len(accum):
                break
    if secretWord == accum:
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    guess_so_far = ''
    for i in secretWord:
        if i not in lettersGuessed:
            guess_so_far += ' _ '
        else:
            guess_so_far += i
    return guess_so_far



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    letter_avail = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            letter_avail += i
        else:
            continue
    return letter_avail
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 8
    lettersGuessed = []
    secretWord = chooseWord(wordlist)
    print(secretWord) # the secret word; please comment out during actual play
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(chooseWord(wordlist))) + " letters long.")
    print("-------------")
    #guesses_left = 8
    #lettersGuessed = []
    #secretWord = chooseWord(wordlist)
    #print(secretWord) # the secret word; please comment out during actual play
    while guesses_left >= 1:
        print("You have " + str(guesses_left) + " guesses left")
        print("Available Letters: " + getAvailableLetters(lettersGuessed), end='')
        guessed_letter = input("Please guess a letter: ")
        guessed_letter = guessed_letter.lower()
        #lettersGuessed += [guessed_letter]
        #print(lettersGuessed)
#        if guessed_letter in secretWord and guessed_letter not in lettersGuessed:
#            lettersGuessed += [guessed_letter]
#            print(lettersGuessed) # to check result, remove or comment later
#            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
#            print("-------------")
#            if isWordGuessed(secretWord, lettersGuessed):
#                break
#            else:
#                continue
        if guessed_letter in secretWord:
            if guessed_letter not in lettersGuessed:
                lettersGuessed += [guessed_letter]
                print(lettersGuessed) # to check result, remove or comment later
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                print("-------------")
                if isWordGuessed(secretWord, lettersGuessed):
                    break
                else:
                    continue
#        elif guessed_letter in lettersGuessed:
#            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
#            print("-------------")
#            continue
        elif guessed_letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            continue     
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed += [guessed_letter]
            print(lettersGuessed) # to check result, remove or comment later
            print("-------------")
        guesses_left -= 1
        
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
        
print(hangman(chooseWord(wordlist)))

