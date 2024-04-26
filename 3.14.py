def reverse_string(input_string):
reversed_string = ""
index = len(input_string) - 1
while index >= 0:
reversed_string += input_string[index]
index -= 1
return reversed_string
input_string = "Hello, World!"
reversed_str = reverse_string(input_string)
print(f"Original String: {input_string}")print(f"Reversed String: {reversed_str}")
