#Storyline : Pie store is busy so there need to be waiting time, after
#waiting for a while the player can choose which pie and afterwards
#the player play for a contest which he gets a random number and
#if it's the lucky number he would get a surprise.



import random
import time

guessesTaken = 0

print('''Welcome at the Raspberry Pie store, today we have a special offer. 
Pick a number and you get the special pie.''')

number = random.randint(1,5)
for Guesstaken in range (5):
    print('Choose a number between 1 and 5 and you will be surprised')
    guess=input()
    guess=int(guess)
    if guess == 1:
        print('Congratulations you will get a Chocolate pie.')
    if guess == 2:
        print('Congratulations you will get a Raspberry pie.')
    if guess == 3:
        print('Congratulations you will get a Blueberry pie.')
    if guess == 4:
        print('Congratulations you will get a Cinnamon blueberry pie.')
    if guess == 5:
        print('Congratulations you will get a Apple pie.')

#Make sure that after 1 guess the user get helped.

print('Could you have a moment please? Than I will get your pie.')
time.sleep(4)

print('Thank you for visiting the Raspberry Pie store. Have a nice day!')




















###############################
#def choosePie():
 #   pie = ''
  #  while pie != 'Chocolate' and pie != 'Raspberry':
   #     print('Which pie do you want? (Chocolate or Raspberry)')
#  pie = input()
#
 #       return pie


#def waiting():
       # print('Currently we are busy, please have patience')
       # time.waiting(5)
      #  print()


#print('Sorry for the waiting time, which type of pie do you want?')
#pie= input()

#Pie = ['Blueberry Pie', 'Chocolate cake', 'Raspberry pie','Apple pie']
#print()
#while pie != ((Blueberry Pie) && (Chocolate cake) && (Raspberry pie) && (apple pie):
     #  print('Which cake do you want?')
      #  pie = input()

      # return pie


