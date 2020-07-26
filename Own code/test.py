import random
import time
#Random number , number connected to a pie.

guessesTaken = 0

print('''Welcome at the Raspberry Pie store, today we have a special offer. 
Pick a number and you get the special pie. May I know your name?''')
myName = input()

print('Excuse me , currently we are busy do you mind to wait for a second?')
time.sleep(3)



pie = ''
if pie< 10:
    if chocolatepie == 'Chocolate':
        print('Chocolatepie')
    else:
        print('Chocolatebar')
elif pie >= 11 and pie <20:
    if pie == 'Raspberry':
        print('RaspberryPie')
    else:
        print('CoconutPie')
else:
    if pie >=20 and pie <30:
        print('Applepie')
    else:
        print('Blueberrypie')

    ###############################
    # def choosePie():
    #   pie = ''
    #  while pie != 'Chocolate' and pie != 'Raspberry':
    #     print('Which pie do you want? (Chocolate or Raspberry)')
    #  pie = input()
    #
    #       return pie

    # def waiting():
    # print('Currently we are busy, please have patience')
    # time.waiting(5)
    #  print()

    # print('Sorry for the waiting time, which type of pie do you want?')
    # pie= input()

    # Pie = ['Blueberry Pie', 'Chocolate cake', 'Raspberry pie','Apple pie']
    # print()
    # while pie != ((Blueberry Pie) && (Chocolate cake) && (Raspberry pie) && (apple pie):
    #  print('Which cake do you want?')
    #  pie = input()

    # return pie


