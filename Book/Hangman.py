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
    print(HANGMAN_PICS)[len(missedLetters)])
    print()
    print('Missed letters:' , end='')
    for letter in missedLetters:            #the for loop on line 50 will iterate over each character in the string missedLetters and print on the screen.
        print(letter,end='')
    print()

    blanks = '_' * len (secretWord)

    for i in range(len(secretWord)):                    # for loop that goes through each letter in secretword and replaces the underscore with the actual letter is it exist in correctLetters.
       if secretWord[i] in correctLetters:
           blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letters in blanks:
        print(letter, end='')
        print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()                   #if the player enters an uppercase letter as a guess , the getguess function will return a lowercase letter.
        if len(guess) != 1:                     #checks whether guess is not one character long.
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess                               #if all these conditions are FALSE then the else statements' block executs and getGuess() returns the valuein guess in line 87.

def playAgain():        #this function returns TRUE if the player wants to play again; otherwise it returns FALSE
    print('Do you want to play again (yes or no)')
    return input().lower().startswith('y')          #.lower returns the lowercase version of the attached string. There is a second method called starts('y) is TRUE.This function returns true if the associated stringbegins with the string parameter between the parentheses and FALSE if it doesn't. The 'yes'.startswith('y') is TRUE.

print('H A N G M A N')          #call that executes when the game is running
missedLetters = ''              #assigned blanks because the player hasn't guessed any missed or correct letters yet.
correctLetters= ''
secretWord= getRandomWord(words)    #will evaluate to a randomly selected word from the words list.
gameIsDone = False                  #when code will set gameIsDone to true when it wants to signal that the game is player over and ask whether they want to play again

while True:                           ##the remainder of the program consist of a while loop . The loop's condition is always tru which meansit will loop forever until it encounters a break statement.
    displayBoard(missedLetters,correctLetters,secretWord)     #calls the displayBoard() function , passing it the three variables . Based on how many letters the player has correctly guessed and missed , this function displays the appropriate Hangman board to the player
    guess = getGuess(missedLetters + correctLetters) #concantese the string in missedLetters and correctLetters variables and passes the result as the argument for the alreadyGuessed parameter
    if guess in secretWord:                 #if the guess string exists in secretWord, then this code concatenates guess to the end of the correctLetters string.
        correctLetters = correctLetters + guess
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    if foundAllLetters:
        print('Yes! The secret word is '' + secretWord +''! You have won ')
        gameIsDone=True
    else:
        missedLetters = missedLetters + guess       #this block will execute if the condition was FALSE .

    if len(missedLetters) == len(HANGMAN_PICS) -1:
        displayBoard(missedLetters, correctLetters, secretWord)
        print('You have run out of guesses!\nAfter' +
              str(len(missedLetters))+'missed guesses and' +
              str(len(correctLetters))+'correct guesses,the word was'
              + secretWord + '"')
        gameIsDone=True

    if gameIsDone:                  #ask if the player want to play again(only if the game is done).
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone= False
            secretWord = getRandomWord(words)

    else:
        break

