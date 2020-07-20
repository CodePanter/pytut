import random

guessesTaken = 0

print('Aloha! What is your name?')
my_name= input()

number = random.randint(1,20)
print('Well,' + my_name + ',I am thinking about a number between 1 and 20.')

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int (guess)

    if guess < number:
        print ('Your guess is too low.')

    if guess > number :
        print('Your guess is too high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('Good job,' + my_name + '!You guessed my number in ' +
          guessesTaken + '  guessess!')

if guess !=number:
    number = str(number)
    print('Nope. The number I was thinking of was  .' + number + '   ')
