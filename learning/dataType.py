a = True
b = False

print(a and b) # False
print(a or b) # True
print(not a) # False
print(not b) # True
print(b or a) # True
print(b and a) # False
print(a and not b) # True
print(not(a or b)) # False

myString = 'my name is felix le, hello everyone'
print(myString[0:8]) # my name
print(myString[0:8:2]) # m ae
print(myString[6:]) # is felix le, hello everyone
print('n' in myString) # True
print('hello' in myString) # True
print(len(myString)) # 31
print(f'Length of myString is {len(myString)}') # Length of myString is 31
# new lines
myNewString= '''This is a new string 
we can use this to write a long string
and it will be printed in multiple lines
. it will stop when we use 3 single quotes

'''
print(myNewString) 
# bytes object
myBytes = b'hello world' # b'hello world'
print(myBytes) # b'hello world'

# Sets

mySet = {1,2,3,4,5,6,7,8,9,10}

newSet = {'a', 'b', 'c'}  # each element is unique, the order doesn't matter
