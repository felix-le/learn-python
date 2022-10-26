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
