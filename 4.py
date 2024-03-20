import math
# Define the variables
x = math.pi  
y = 2       

# Calculate the product of x and y
z = x * y

print(f"Multiplying {x:.5f} and {y} gives {z:.3f}.")


nums = [2, 5, 6, 8, 11]

# Initialize an empty list
squares = []

# Calculate the square of each number and append it to the 'squares' list
for num in nums:
    square = num ** 2
    squares.append(square)

# Print the list of squares
print("Squares of numbers in the 'nums' list:", squares)
