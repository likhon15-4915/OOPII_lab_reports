def reverse_print(lst, index):
if index < 0:
return
print(lst[index])
reverse_print(lst, index - 1)
my_list = [15,16,19,23]
reverse_print(my_list, len(my_list) - 1)
