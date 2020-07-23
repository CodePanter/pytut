a = [3,10,-1,4]
print(a)

a.append(1) #a.append adds numbers to the lists datatype.
print(a)

a.append('hello') # you can mix types in a list, for example with a string.
print(a)

a.append([2,31,45,5]) # You can also add a list to a list.
print(a)

a.pop() # Function to delete the last item added on the list.
print(a)

a.pop()
print(a)

print(a[0])# Use this function to get a certain element, it starts with index 0.

a[0] = 1000 # Assign new value , 0 is the index number so which number you want to change and after = is the number you want instead.

print(a)

b = ["banana","apple","microsoft"] # challenge to swap the last item to the list to the first place.
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)

b[0], b[2] = b[2],b[0]
print(b)