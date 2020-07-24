#Storyline : Pie store is busy so there need to be waiting time, after
#waiting for a while the player can choose which pie and afterwards
#the player play for a contest which he gets a random number and
#if it's the lucky number he would get a surprise.



import random
import time

guessesTaken = 0

print('''Welcome at the Raspberry Pie store, today we have a special offer. Pick a number and you get the special pie.''')
myNumber=input()
print()

def choosePie():
    pie = ''
    while pie != 'Chocolate' and pie != 'Raspberry':
        print('Which pie do you want? (Chocolate or Raspberry)')
        pie = input()

        return pie


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


