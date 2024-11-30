def reverse_tuple(input_tuple): 
reversed_list = [] 
for i in range(len(input_tuple) - 1, -1, -1): 
reversed_list.append(input_tuple[i]) 
reversed_tuple = tuple(reversed_list) 
return reversed_tuple 
example_tuple = (1, 2, 3, 4, 5) 
reversed_tuple = reverse_tuple(example_tuple) 
print("Reversed Tuple:", reversed_tuple) 
