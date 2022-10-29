# Data types

```python
# set
newSet = {'a', 'b', 'c'}  # each element is unique, the order doesn't matter

# list
newList = ['a', 'b', 'c']  # each element can be repeated, the order matters

# tuple
newTuple = ('a', 'b', 'c')  # each element can be repeated, the order matters. You can't change the elements, but you can change the whole tuple

myTuple = 1,2,3,4,5  # you can also create a tuple without the parenthesis


# Tuple can be a function argument, but list can't
def func(a, b, c):
    print(a, b, c)

# dictionaries are a collection of key-value pairs
# they are unordered, mutable, and indexed
# they are also known as associative arrays or hashes
animals = {
  'c': 'cat',
  'd': 'dog',
  'b': 'bird',
  'f': 'fish'
}

```

# Work flow

```python
print(['FizzBuzz' if n %15 == 0 else 'Fizz' if n%3 ==0 else 'Buzz' if n % 5 == 0 else n for n in range (1,101)])
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz', 31, 32, 'Fizz', 34, 'Buzz', 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'FizzBuzz', 46, 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58, 59, 'FizzBuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz', 'Buzz', 71, 'Fizz', 73, 74, 'FizzBuzz', 76, 77, 'Fizz', 79, 'Buzz', 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'FizzBuzz', 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']


# while loop
from datetime import datetime

wait_until = datetime.now().second + 1

while datetime.now().second != wait_until:
    pass
print(f'We are at {wait_until} seconds')

# break

while True:
  if datetime.now().second == wait_until:
    print(f'We are at {wait_until} seconds')
    break

# continue

while True:
  if datetime.now().second < wait_until:
    continue
  break
print(f'We are at {wait_until} seconds')


```
