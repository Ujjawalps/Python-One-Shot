# Demonstrating input in Python and using built-in string methods

# Basic input
# name = input("Enter your name: ")
# print("Hello,", name)

# Input with stripping whitespace
# raw_input = input("Enter something with spaces around: ")
# trimmed_input = raw_input.strip()
# print("Trimmed input:", trimmed_input)

# Splitting input into a list
numbers = input("Enter numbers separated by commas: ")
num_list = numbers.strip().split(",")
print("List of numbers:", num_list)

# # Converting input to integer
# age = int(input("Enter your age: ").strip())
# print("Your age is:", age)

# # Using replace to clean input
dirty_input = input("Enter a string with unwanted characters (e.g., '*hello*'): ")
clean_input = dirty_input.replace('*', '').strip()
print("Cleaned input:", clean_input)