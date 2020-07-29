a = ['apple','banana','cherry']
for element in a:
    print(element)

for i in range(len(a)):    #return the length of a
    print(a[i])

for i in range(len(a)):    #return the length of a
    for j in range(i +1): #i = 0 -> j , i=1i>j= 0,1 , i=2->j=0,1,2
     print(a[i])

#can you compute the sum of all multiples of 3 and 5 that are less than 100?
total=0
for i in range(1,100):
    if i % 3 == 0:          # if i is a multiple of 3
        total += i
    elif i % 5 == 0:
        total += i
print(total)

total=0
for i in range (1,100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


#given an list and showing only the negative numbers
given_list = [7,2,5,6,-3,-5,-2,-7,1,3,-5,-8]
total2=0
j = len(given_list) -1
while given_list[j] < 0:    #while the current element which is examining is less than 0
    total2 += given_list[j]
    j -= 1
print(total2)