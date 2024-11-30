def create_squares_dictionary(lst): 
squares_dict = {num: num**2 for num in lst} 
return squares_dict 
integer_list = [1, 2, 3, 4, 5] 
squares_dictionary = create_squares_dictionary(integer_list) 
print("Dictionary with elements and their squares:") 
print(squares_dictionary) 
