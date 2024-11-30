def character_frequency(string): 
frequency_dict = {} 
for char in string: 
if char in frequency_dict: 
frequency_dict[char] += 1 
else: 
frequency_dict[char] = 1 
return frequency_dict 
input_string = input("Enter a string: ") 
frequency_dict = character_frequency(input_string) 
print("Character frequency dictionary:") 
for char, frequency in frequency_dict.items(): 
print(f"{char}: {frequency}") 
