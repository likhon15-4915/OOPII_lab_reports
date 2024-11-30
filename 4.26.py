def count_key_value_pairs(dictionary): 
count = 0 
for value in dictionary.values(): 
if isinstance(value, dict): 
count += count_key_value_pairs(value)   
count += len(dictionary)   
return count 
nested_dict = { 
'a': 1, 
'b': {'c': 2, 'd': 3}, 
'e': {'f': {'g': 4, 'h': 5}}, 
'i': 6 
} 
total_pairs = count_key_value_pairs(nested_dict) 
print("Total number of key-value pairs:", total_pairs) 
