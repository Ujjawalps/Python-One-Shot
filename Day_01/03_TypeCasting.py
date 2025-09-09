# Type Casting in Python

# Implicit Type Casting (Python automatically converts types)
a = 10      # Integer
b = 2.5     # Float

result = a + b  # 'a' is implicitly cast to float
print(result)   # Output: 12.5

# Explicit Type Casting (Manually converting types)
x = "100"       # String
y = int(x)      # Convert string to integer
print(y + 50)   # Output: 150

# Converting float to integer
z = 9.8
z_int = int(z)  # Truncates decimal part
print(z_int)    # Output: 9

# Converting integer to string
num = 42
num_str = str(num)
print("The answer is " + num_str)  # Output: The answer is 42


# Converting string to boolean
str_true = "True"
bool_value = bool(str_true)  # Non-empty string is always True
print(bool_value)            # Output: True

str_empty = ""
bool_empty = bool(str_empty) # Empty string is False
print(bool_empty)            # Output: False

# Converting boolean to string
flag = False
flag_str = str(flag)
print("Flag value is " + flag_str)  # Output: Flag value is False

# Converting integer to string
num2 = 123
num2_str = str(num2)
print("Number: " + str(type(num2_str)))        # Output: Number: <class 'str'>
print(num2_str + '50')                # Output: 12350 (string concatenation)

# Converting float to string
flt = 3.1415
flt_str = str(flt)
print("Pi is " + flt_str)           # Output: Pi is 3.1415


print(type(type(num2_str)))  # Output: <class 'type'>... type() returns the type of the object