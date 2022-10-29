# list comprehension
myNumbers  = [2,3,4,5]
myNewList = [x * 2 for x in myNumbers]
print(myNewList) # [4, 6, 8, 10]
 

# list comprehension with filters
myNumbers  = [2,3,4,5]
myNewList = [x * 2 for x in myNumbers if x > 3]
print(myNewList) # [8, 10]

# list comprehension with multiple filters
myNumbers  = [2,3,4,5]
myNewList = [x * 2 for x in myNumbers if x > 3 if x < 5]
print(myNewList) # [8]

# list comprehension with split
myString = 'hello 12345 world'
myNewList = [x for x in myString.split() if x.isdigit()]
print(myNewList) # ['12345']

myStringList = myString.split()
print(myStringList) # ['hello', '12345', 'world']

# with functions
def cleanWord(word):
  return word.strip().lower()

myString = '  Hello 12345 World  '
myNewList = [cleanWord(x) for x in myString.split()]
print(myNewList) # ['hello', '12345', 'world']


# Nested list comprehension
myNumbers = [1,2,3,4,5]
myNewList = [[x, x * 2] for x in myNumbers]
print(myNewList) # [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]]
