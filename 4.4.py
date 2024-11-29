def count_element_frequency(nested_list):
flat_list = flatten_list(nested_list)
frequency = Counter(flat_list)
return frequency
