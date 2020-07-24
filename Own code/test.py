import random
import time
#Random number , number connected to a pie.

guessesTaken = 0

print('''Welcome at the Raspberry Pie store, today we have a special offer. 
Pick a number and you get the special pie. May I know your name?''')
myName = input()

print('Excuse me , currently we are busy do you mind to wait for a second?')
time.sleep(3)

print()


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