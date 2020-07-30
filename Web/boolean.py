  #used to find the type
type(3)

a = 3
b = 1

if a > b:                           #if true prints a is greater than b
    print('a is greater than b')



if True:
    print ('a is greater than b')

boolean_value= a>b
print(boolean_value)

if boolean_value:
    print('a is greater than b')

def are_you_sad(is_rainy,has_umbrella):
    return is_rainy and not has_umbrella #you are only sad or you  got only true when is raining is true and has umbrella is false
are_you_sad(True,False)

def c_greater_than_d_plus_e(c,d,e):
    if c > d + e:
        return True
    else:
        return False
c_greater_than_d_plus_e(3,1,1)

c_greater_than_d_plus_e(3,1,2)