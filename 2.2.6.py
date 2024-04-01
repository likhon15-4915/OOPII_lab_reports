def first_occurrence_index(lst, target):
 for i, num in enumerate(lst):
 if num == target:
 return i
 return -1
lst = input("Enter the elements of the list separated by spaces: ").split()
lst = [int(num) for num in lst]
target_value = int(input("Enter the target value: "))
index = first_occurrence_index(lst, target_value)
if index != -1:
 print(f"The target value {target_value} appears for the first time at index:{index}")
else:
 print(f"The target value {target_value} is not present in the list.")
