def extract_slice(input_tuple, start, end): 
if start < 0 or end > len(input_tuple): 
print("Invalid indices for slicing.") 
return None 
sliced_tuple = input_tuple[start:end] 
return sliced_tuple 
example_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
start_index = 2 
end_index = 6 
sliced_elements = extract_slice(example_tuple, start_index, end_index) 
print("Sliced Elements:", sliced_elements) 
