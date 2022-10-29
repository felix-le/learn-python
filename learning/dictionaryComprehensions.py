# dictionary comprehension

# create a dictionary with each item being a pair of a number and its square
squares = {x: x**2 for x in range(6)}
print(squares) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

animalList = [('a', 'ant'), ('d', 'dog'), ('c', 'cat')]

animals = {item[0]: item[1] for item in animalList}
print(animals) # {'a': 'ant', 'd': 'dog', 'c': 'cat'}

# OR
animals = {k: v for k, v in animalList}
print(animals) # {'a': 'ant', 'd': 'dog', 'c': 'cat'}

print(animals.items()) # dict_items([('a', 'ant'), ('d', 'dog'), ('c', 'cat')])
print(animals.keys()) # dict_keys(['a', 'd', 'c'])

print(list(animals.items())) # [('a', 'ant'), ('d', 'dog'), ('c', 'cat')]

# OR
animals = [{'letter': key, 'name': value} for key, value in animalList]
print(animals) # [{'letter': 'a', 'name': 'ant'}, {'letter': 'd', 'name': 'dog'}, {'letter': 'c', 'name': 'cat'}]

# OR
animals = [{'letter': key, 'name': value} for key, value in animalList if key != 'd']
print(animals) # [{'letter': 'a', 'name': 'ant'}, {'letter': 'c', 'name': 'cat'}]
