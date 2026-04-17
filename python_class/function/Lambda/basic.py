# input list
numbers = [1, 2, 3, 4, 5]

# assert to check list is not empty
assert len(numbers) > 0, "List is empty!"

# using lambda with map to find squares
squares = list(map(lambda x: x**2, numbers))

# display result
print("Original list:", numbers)
print("Squared list:", squares)