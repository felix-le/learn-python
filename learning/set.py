
mySet = {1,2,3,4,5,6,7,8,9,10}

newSet = {'a', 'b', 'c'}  # each element is unique, the order doesn't matter
newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # [::2], [0:6:2], [3:], [:6], [::-1], [7:]

mySet = set(('a', 'b', 'c'))
print(mySet) # {'a', 'c', 'b'}
myListSet = set(newList) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

mySet.add('d') # {'a', 'c', 'b', 'd'}
mySet.remove('a') # {'c', 'b', 'd'}
mySet.discard('b') # {'c', 'd'}
mySet.pop() # {'d'}
mySet.clear() # set()
mySet.update(newSet) # {'a', 'c', 'b'}
mySet.update(newList) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mySet.update(newList, newSet) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'c', 'b'}
mySet.update(newList, newSet, 'hello') # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'c', 'b', 'l', 'e', 'h', 'o'}
mySet.difference_update(newList) # {'a', 'c', 'b', 'l', 'e', 'h', 'o'}
print('a' in mySet) # True
print('z' in mySet) # False
len(mySet) # 7