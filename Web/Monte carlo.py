import random

def random_walk_2(n):
    'Return coordinates after n block random walk'

    x,y=0,0
    for i in range(n):
        (dx,dy)= random.choice([(0,1),(0,-1),(1,0),(-1,0)])   #difference in y, difference in x
        x += dx #shortcut for x=x+dx
        y += dy
        return (x,y)

    #What is the longest random walk you can take so that on average you  will end up 4 blocks or fewer from home?

number_of_walks = 10000

for walk_length in range (1,31):    #in range are the amount of blocks
    no_transport = 0 #number of walks 4 or fewer from home

    #Monte carlo loop of 10 000 samples
    for i in range(number_of_walks):
        (x,y) = random_walk_2(walk_length) #The length of the walk
        distance = abs(x) + abs(y)                           #distance from home
        if distance <= 4:           #if distance is less or equal than 4
            no_transport += 1       #than increment the no transport counter
        no_transport_percentage = float (no_transport)/ number_of_walks #compute random walks with a walk to home
        print('Walks size =', walk_length,
              '/ % of no transport = ',100 *no_transport_percentage )


