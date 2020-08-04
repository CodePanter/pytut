import random
HANGMAN_PICS =  [ '''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''','''
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       === ''','''  
    +---+
    O   |
   /|\  |
        |''','''
       ===
    +---+
    O   |
   /|\  |
   /    |
    +---+''','''
    O   |
   /|\  |
   / \  |
       ===''']

words = 'ant baboon badger beaver camel cat clam cobra cougar' \
        'coyote crow deer dog donkey duck eagle ferret fox frog' \
        'goat goose hawk lion lizzard llama mole monkey moose mouse' \
        'mule newt otter owl panda parrot pigeon python rabbit ram rat' \
        'raven rhino salmon seal shark sheep skunk sloth snake spider stork' \
        'swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordlist):                                                    #defined a getRandomWord function, a list argument will be passed for its wordList parameter.This function will return a single secret word from the list in wordList.
    #This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordlist) -1 )                             #Store a random index for this list in the wordIndex variable calling randint() with 2 arguments. First 0(for the first possible index) and the second is the value that the expression len(wordList)-1 evaluates to (for the last possible index in a wordlist.
    return wordlist[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):    #missedletters= a string of the letter that is not in a secret word. correctletters= a string of the letters the playet guessed that are in the secret word. secretword= a string of the secret word that the player is trying to guess.
    print(HANGMAN_PICS)[len(missedLetters)]
    print()
    print('Missed letters:' , end='')
    for letter in missedLetters:            #the for loop on line 50 will iterate over each character in the string missedLetters and print on the screen.
        print(letter,end='')
    print()
