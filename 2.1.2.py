def calculate_ascii_sum(name):
 ascii_sum = sum(ord(char) for char in name)
 return ascii_sum
employee_names = ["Umme","Eity","Esrat"]
numerical_values = []
for name in employee_names:
 ascii_sum = calculate_ascii_sum(name)
 numerical_values.append(ascii_sum)
print("Numerical Values:", numerical_values)
