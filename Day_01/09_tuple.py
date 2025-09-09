# Tuples in Python

# Creating a tuple
my_tuple = (1, 2, 2, 3, "apple", True)

# Tuple methods
print(my_tuple.count(2)) 

print(my_tuple.index("apple")) 



# Accessing elements
print(my_tuple[0])      # Output: 1
print(my_tuple[-1])     # Output: True

# Slicing a tuple
print(my_tuple[1:4])    # Output: (2, 3, 'apple')

# Tuples are immutable
# my_tuple[0] = 10      # This will raise a TypeError

# Length of a tuple
print(len(my_tuple))    # Output: 5

# Iterating over a tuple
for item in my_tuple:
    print(item)

# Nested tuples
nested_tuple = (1, (2, 3), (4, 5))
print(nested_tuple[1])  # Output: (2, 3)

# Tuple unpacking
a, b, c, d, e, f = my_tuple
print(a, d)             # Output: 1 apple

# Using tuple in functions
def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max((5, 2, 8, 1))
print(result)           # Output: (1, 8)