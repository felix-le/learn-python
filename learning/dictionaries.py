# dictionaries

# dictionaries are a collection of key-value pairs
# they are unordered, mutable, and indexed
# they are also known as associative arrays or hashes
animals = {
  'c': 'cat',
  'd': 'dog',
  'b': 'bird',
  'f': 'fish'
}

# call the dictionary
print(animals) # {'c': 'cat', 'd': 'dog', 'b': 'bird', 'f': 'fish'}
print(animals['c']) # cat 
#OR use get() method
print(animals.get('c')) # cat
# change value
animals['c'] = 'cow'
print(animals) # {'c': 'cow', 'd': 'dog', 'b': 'bird', 'f': 'fish'}
# add new key-value pair
animals['h'] = 'horse'
print(animals) # {'c': 'cow', 'd': 'dog', 'b': 'bird', 'f': 'fish', 'h': 'horse'}
# call all keys
print(animals.keys()) # dict_keys(['c', 'd', 'b', 'f', 'h'])
# call all values
print(animals.values()) # dict_values(['cow', 'dog', 'bird', 'fish', 'horse'])

# convert to list
print(list(animals.keys())) # ['c', 'd', 'b', 'f', 'h']
# get len
print(len(animals)) # 5
# remove item
animals.pop('c')
print(animals) # {'d': 'dog', 'b': 'bird', 'f': 'fish', 'h': 'horse'}
# remove last item
animals.popitem()
print(animals) # {'d': 'dog', 'b': 'bird', 'f': 'fish'}
# remove all items
animals.clear()
print(animals) # {}

# copy dictionary
animals = {
  'c': 'cat',
  'd': 'dog',
  'b': 'bird',
  'f': 'fish'
}
animals2 = animals.copy()

# nested list
animals = {
  'c': 'cat',
  'd': 'dog',
  'b': 'bird',
  'f': 'fish',
  'l': ['lion', 'leopard', 'lynx']
}
# add new item to nested list
animals['l'].append('lizard')
print(animals) # {'c': 'cat', 'd': 'dog', 'b': 'bird', 'f': 'fish', 'l': ['lion', 'leopard', 'lynx', 'lizard']}
# remove item from nested list
animals['l'].remove('lion')
print(animals) # {'c': 'cat', 'd': 'dog', 'b': 'bird', 'f': 'fish', 'l': ['leopard', 'lynx', 'lizard']}

# dictionary constructor
animals = dict(c='cat', d='dog', b='bird', f='fish')
print(animals) # {'c': 'cat', 'd': 'dog', 'b': 'bird', 'f': 'fish'}
# OR
animals = dict([('c', 'cat'), ('d', 'dog'), ('b', 'bird'), ('f', 'fish')])
print(animals) # {'c': 'cat', 'd': 'dog', 'b': 'bird', 'f': 'fish'}

#  the default dict
from collections import defaultdict
# create a dictionary with a default value
animals = defaultdict(int)
animals['o'] = 1
animals['t'] = 2
print(animals) # defaultdict(<class 'int'>, {'o': 1, 't': 2})

#  default dict with list
animals = defaultdict(list)
animals['c'].append('cat')
animals['d'].append('dog')
animals['b'].append('bird')
animals['f'].append('fish')
print(animals) # defaultdict(<class 'list'>, {'c': ['cat'], 'd': ['dog'], 'b': ['bird'], 'f': ['fish']})