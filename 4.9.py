def count_frequency(tuple_data, element):
 count = 0
 for item in tuple_data:
 if item == element:
 count += 1
 return count
example_tuple = (1, 2, 3, 4, 1, 1, 2, 3, 4, 5)
element_to_find = 1
frequency = count_frequency(example_tuple, element_to_find)
print("Frequency of", element_to_find, ":", frequency)
