fruits = ['apple', 'banana', 'cherry', 'date']

# lists are mutable and ordered
print(fruits)  

print(fruits[0])  
print(fruits[-1])  

# Slicing
print(fruits[1:3])  
print(fruits[:2])  
print(fruits[2:])  

# here are some common list methods
fruits.append('coconut')  
print(fruits)  

new_fruits = fruits.copy()  
print(new_fruits)

fruits.insert(1, 'blueberry')
print(fruits)

fruits.remove('date') # Remove by value
print(fruits)

fruits.pop()  # Remove last item
print(fruits)

fruits.pop(1)  # Remove item at index 1
print(fruits)

fruits.clear()  # Remove all items
print(fruits)
