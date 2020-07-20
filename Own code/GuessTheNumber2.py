import random

print ('Welcome , what is your name ?)
my_name = input()

print('Which number do you think it is?)
guess_number = input()

guess_number = int (input())
if (guess_number % 2 ) == 0:
    print('{0} is Even'.format(guess_number))
else:
    print('{0} is Odd'.format(guess_number))