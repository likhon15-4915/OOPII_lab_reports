def list_manipulation(numbers):
total_sum = sum(numbers)
average = total_sum / len(numbers)
maximum = max(numbers)
minimum = min(numbers)
return total_sum, average, maximum, minimum
numbers = [5, 10, 15, 20, 25]
total_sum, average, maximum, minimum = list_manipulation(numbers)
print(f"Sum: {total_sum}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
