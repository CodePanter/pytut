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

def getRandomWord(wordlist):
    #This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordlist) -1 )
    return wordlist[wordIndex]
