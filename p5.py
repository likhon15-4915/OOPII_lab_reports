#items
item_names = ["Pen", "BOok", "marKer"]

# Case 01: Find out the length of each item and store in another list

item_lengths = [len(item) for item in item_names]
print(item_lengths)

# Case 02: Access each item's name and convert the case of letters
for item in item_names:
    print(item.upper())  # Convert to uppercase
    print(item.lower())  # Convert to lowercase
