def flatten_list(nested_list):
 flat_list = []
 for sublist in nested_list:
 for item in sublist:
 flat_list.append(item)
 return flat_list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat_list = flatten_list(nested_list)
print("Flat List:", flat_list)
