total= 0
for i in range(1,5):
    total += i
print(total)

total2 = 0
j = 1
while j<5 :     #while j is less than 5
    total2 += j #add j to the total2 variable
    j += 1      #Add 1 to j
print(total2)

given_list = [4,4,6,1,5,6,-2,-6,1,5,9]
#give a sum of only the positive numbers in the list

total3 = 0
i = 0
while given_list [i] > 0:   #First check the element in the current list
    total3 += given_list[i] #do the following : add the current element to total
    i += 1                  # go to the next item
print(total3)


#give a sum of only positive numbers in the list without negative numbers

given_list = [5,3,1,4,5,6]
total4 = 0
i = 0
while i < 5 and given_list[i] > 0:
    total4 += given_list[i]
    i+=1
print(total4)