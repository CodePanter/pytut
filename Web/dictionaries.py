d = {} # d= {'George':24 ,'Tom:' 34' }
d['George'] = 24
d['Tom'] = 32
d['Jenny'] = 21

print(d['George']) #prints value of variable George
print(d['Jenny'])

d['Jenny'] = 20     #way to assign a new value to the variable
print(d['Jenny'])


#keys are commonly string or numbers
d[10]=100
print(d[10])

#how to iterate over key-value pairs?
for key, value in d.items():
    print('Key')
    print(key)
    print ('Value:')
    print(value)
    print('')