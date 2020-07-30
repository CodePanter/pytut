class Robot:
    def __init__(self,name,color,weight):#constructor
     self.name=name
     self.color=color
     self.weight=weight

    def introduce_self(self):
        print('My name is ' + self.name)

#r1 = Robot()
#r1.name = 'Tom'
#r1.color = 'red'
#r1.weight = 30

#r2 = Robot()
#r2.name = 'Jerry'
#r2.color = 'blue'
#r2.weight = 40

r1= Robot ('Tom','Red', 30)
r2= Robot ('Jenny','Blue', 40)


r1.introduce_self()
r2.introduce_self()