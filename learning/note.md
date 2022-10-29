# Data types

```python
# Boolean
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
```

## Strings

```python
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
```

# Lists

```python
myList = [1,2,3,4,5,6,7,8,9,10]
myNewList = list(range(100)) # only to 99

print(myList[3:])
print(myList[0:6:2])
print(myList[::2])

print(myNewList[::-10])  # Reverse list [99, 89, 79, 69, 59, 49, 39, 29, 19, 9]
```

## Modifying lists

```python
myList.append(11) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

myList.insert(0, 'a new value')  # ['a new value', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

myList.remove('a new value') # [ 1, 2, 3, 4, 6, 7, 8, 9, 10, 11]

x = myList.pop() # [ 1, 2, 3, 4, 6, 7, 8, 9, 10]
x # 11
myList # [ 1, 2, 3, 4, 6, 7, 8, 9, 10]
```

# Tuples and sets

```python


```
