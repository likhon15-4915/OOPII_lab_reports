# Given list of numbers
numbers = [1, 2, 3, 4, 5]

# Swap adjacent items in pairs
for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

# Print the resulting list
print(numbers)
