import time

def displayintro():
    print('Welcome to the local store BlueBerry Pie, currently we are quite busy do you mind to wait?.')


def waiting():
    print('Currently we are busy, please have patience')
    time.waiting(5)
    print()

def choosePie():
    print('Sorry for the waiting time, which type of pie do you want?')
    pie = ['Blueberry Pie', 'Chocolate cake', 'Raspberry pie','Apple pie']
    print(pie)

    while pie != 'Blueberry Pie' and 'Chocolate cake' and 'Raspberry pie' and 'apple pue':
        print('Which cake do you want?')
        pie = input()

        return pie


