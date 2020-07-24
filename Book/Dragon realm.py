import random
import time

def displayIntro():
    print('Welcome in a world full of pitbulls , some are scary but some are actually sweet.')
    print()

def chooseCave():
    cave = ''
        # A local scope is created whenever a function is called. Any variables assigned in this function exist within the local scope. Think of a scope as a container for variables. What makes variables in local scopes special is that they are forgotten when the function returns and they will be re-created if the function is called again.
    while cave != '1' and cave != '2':
        # a While loop repeats as long as a certain condition is true, when the execution reaches a while statement , it evaluates the condition next to the while keyword. If the condition evaluates true , the execution moves inside the following block, called the while block. If the condition evaluates to False , the execution past the while block.
        # == & =! are comparison operators, the AND operator is a Boolean operator. The and operator can be used to evaluate any two Boolean expressions.
        #The condition has two parts connected by the AND Boolean operator . The condition is True only if both parts are true.
        print('Which cave will you go into, 1 or 2?')
        cave = input()

    return cave
        #A return statement appears only inside def blocks where a function(chooseCave) is defined.


def checkCave(chosenCave):
    print('You approach the cave....')
    time.sleep(2)            #Time module has a function called sleep that pauses th program.
    print('It is dark and spooky ...')
    time.sleep(2)
    print('A large pitbull jumps out in front of you! He opens his jaws and ...')
    time.sleep(2)
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)
        #randint function will randomly return either 1 or 2.

    if chosenCave == str(friendlyCave):
        # Checks whether the player
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()
