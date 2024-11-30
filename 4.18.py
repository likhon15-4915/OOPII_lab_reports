def search_item_by_price(items, price): 
for item, item_price in items.items(): 
if item_price == price: 
return item 
return None 
items_prices = { 
"banana": 1.50, 
"grapes": 0.75, 
"apple": 1.20, 
"mango": 2.00, 
"watermelon": 3.50 
} 
desired_price = 1.20 
found_item = search_item_by_price(items_prices, desired_price) 
if found_item: 
print(f"Item with price ${desired_price}: {found_item}") 
else: 
print(f"No item found with price ${desired_price}")
