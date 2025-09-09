# Demonstration of loops in Python

# 1. While Loop: Executes as long as the condition is True
count = 0
while count < 5:  # The loop runs while 'count' is less than 5
    print(f"While loop iteration: count = {count}")
    count += 1  # Increment count to eventually break the loop

print("While loop finished.\n")

# 2. For Loop with range(): Iterates over a sequence of numbers
# range(start, stop, step) generates numbers from start to stop-1, incremented by step
for i in range(0, 5):  # i takes values 0, 1, 2, 3, 4
    print(f"For loop iteration: i = {i}")

print("For loop finished.\n")

# 3. For Loop with custom step
for i in range(0, 10, 2):  # i takes values 0, 2, 4, 6, 8
    print(f"For loop with step 2: i = {i}")

print("Custom step for loop finished.")