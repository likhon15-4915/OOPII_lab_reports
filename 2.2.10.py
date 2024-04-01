def uni_srt_lst(list1, list2):
 combined_list = list1 + list2
 element_count = {}
 for num in combined_list:
 element_count[num] = element_count.get(num, 0) + 1
 unique_list = [num for num, count in element_count.items() if count == 1]
 unique_list.sort()
 return unique_list
list1 = [1, 4, 5, 6, 7,9]
list2 = [2, 1, 3, 4, 5,12]
newlist = uni_srt_lst(list1, list2)
print("New list with unique values, sorted:", newlist)
