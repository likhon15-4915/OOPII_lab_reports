def remove_item(items, item_name): 
if item_name in items: 
del items[item_name] 
print(f"{item_name} has been removed from the dictionary.") 
else: 
print(f"{item_name} is not in the dictionary.") 
items_quantities = { 
"apple": 5, 
"banana": 3, 
"orange": 7, 
"grapes": 10, 
"watermelon": 2 
} 
item_to_remove = input("Enter the name of the item you want to remove: ") 
remove_item(items_quantities, item_to_remove) 
print("Updated dictionary:", items_quantities) 
