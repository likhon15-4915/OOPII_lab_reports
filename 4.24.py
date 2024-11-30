def check_key(dictionary, key): 
if key in dictionary: 
print("Key Found") 
else: 
print("Key Not Found") 
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
input_key = input("Enter the key to check: ") 
check_key(sample_dict, input_key)
