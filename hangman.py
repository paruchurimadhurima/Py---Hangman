import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
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


wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in secretWord :
        if i not in lettersGuessed :
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    str=""
    for i in secretWord :
        if i in lettersGuessed :
            str=str+i
        else :
            str=str+"_"
            str=str+" "
    return str


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str=""
    for i in ("abcdefghijklmnopqrstuvwxyz") :
        if i not in lettersGuessed :
            str=str+i
    return str

def check_guess_validity(lettersGuessed,letterGuessed):
    '''
    checks wether the letterGuessed is in lettersGuessed or not
    if it is present return true else false
    '''
    if letterGuessed in lettersGuessed :
        return True
    else :
        return False

def check_guess(secretWord,letterGuessed) :
    '''
        checks wether the letterGuessed is in secretWord or not
        if it is present return true else false
    '''
    if letterGuessed in secretWord :
        return True
    else :
        return False

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
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord) ,"letters long.")
    print("-------------")
    flag=1
    guess = 8
    lettersGuessed=""
    while (guess) :
        print("You have", guess ,"guesses left.")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        letterGuessed=str(input("Please guess a letter: "))
        letterGuessed=letterGuessed.lower()
        if (check_guess_validity(lettersGuessed,letterGuessed)) :
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        elif (check_guess(secretWord,letterGuessed)) :
            lettersGuessed = lettersGuessed + letterGuessed
            print("Good guess: ",getGuessedWord(secretWord, lettersGuessed))
        else :
            lettersGuessed = lettersGuessed + letterGuessed
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            guess=guess-1
        print("-------------")
        if (isWordGuessed(secretWord, lettersGuessed)) :
            print("Congratulations, you won!")
            break
    if guess==0 :
        print("Sorry, you ran out of guesses. The word was",secretWord,".")
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)


